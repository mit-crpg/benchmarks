#!/usr/bin/env python

import numpy as np

import openmc
import openmc.checkvalue as cv
from make_library import GROUP_STRUCT

MAT_NAMES = ['PU', 'U', 'UD2O', 'UAL', 'URR', 'H2O', 'Fe-Na']
GROUPS = [1, 2, 3, 6]
GROUP_FILES = {g: str(g) + 'g.h5' for g in GROUPS}
ORDER = [0, 1, 2]
GEOM = ['IN', 'SL', 'CY', 'SP', 'ISLC', 'SL-NS', 'FENA']
INF = 1.e50


class Case(object):
    """Stores the model data for a particular case
    """

    def __init__(self, num, name, mat_names, groups, order, geom, rad, ref_k,
                 params):
        cv.check_value('groups', groups, GROUPS)
        cv.check_value('order', order, ORDER)
        cv.check_value('groups', groups, GROUPS)
        cv.check_value('geom', geom, GEOM)
        self.number = num
        self.name = name
        self.mat_names = mat_names
        self.groups = groups
        self.order = order
        self.geom = geom
        self.rad = rad
        self.ref_k = ref_k
        self.mesh_dim = params['mesh_dim']
        self.batches = params['batches']
        self.inactive = params['inactive']
        self.particles = params['particles']
        if 'tab_leg' in params:
            self.tab_leg = params['tab_leg']
        else:
            self.tab_leg = None
        if 'tally' in params:
            self.tally = params['tally']
        else:
            self.tally = False

    def make_materials(self):
        materials_file = openmc.Materials()

        mats = []
        macros = []
        for i in range(len(self.mat_names)):
            macros.append(openmc.Macroscopic(self.mat_names[i]))
            mats.append(openmc.Material(name=self.mat_names[i]))
            mats[-1].set_density('macro', 1.0)
            mats[-1].add_macroscopic(macros[-1])
            materials_file += [mats[-1]]

        materials_file.cross_sections = GROUP_FILES[self.groups]

        return mats, materials_file

    def make_settings(self):
        # Instantiate a Settings object, set all runtime parameters
        settings_file = openmc.Settings()
        settings_file.energy_mode = "multi-group"
        if self.tab_leg:
            settings_file.tabular_legendre = self.tab_leg
        settings_file.batches = self.batches
        settings_file.inactive = self.inactive
        settings_file.particles = self.particles
        if self.order > 0:
            settings_file.max_order = self.order
        if self.geom in ['SL', 'ISLC']:
            bounds = [-self.rad[0], -INF, -INF, self.rad[0], INF, INF]
            uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:])
        elif self.geom == 'SL-NS':
            bounds = [-self.rad[0], -INF, -INF, self.rad[0], INF, INF]
            uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:],
                                            only_fissionable=True)
        elif self.geom == 'IN':
            bounds = [-INF, -INF, -INF, INF, INF, INF]
            uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:])
        elif self.geom == 'CY':
            bounds = [-self.rad[0], -self.rad[0], -INF,
                      self.rad[0], self.rad[0], INF]
            uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:],
                                            only_fissionable=True)
        elif self.geom == 'SP':
            bounds = [-self.rad[0], -self.rad[0], -self.rad[0],
                      self.rad[0], self.rad[0], self.rad[0]]
            uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:],
                                            only_fissionable=True)
        elif self.geom == 'FENA':
            bounds = [0., -INF, -INF, self.rad[-1], INF, INF]
            uniform_dist = openmc.stats.Box(bounds[:3], bounds[3:],
                                            only_fissionable=True)
        else:
            raise NotImplementedError

        settings_file.source = openmc.source.Source(space=uniform_dist)

        settings_file.output = {'summary': False}

        return settings_file

    def make_tallies(self, r=None):
        if not self.tally:
            return None

        if self.geom == 'IN':
            return None

        # Instantiate a tally mesh
        mesh = openmc.Mesh(mesh_id=1)
        mesh.type = 'regular'
        mesh.dimension = self.mesh_dim
        if self.geom == 'SL' or self.geom == 'ISLC':
            mesh.lower_left = [-r, -INF, -INF]
            mesh.upper_right = [r, INF, INF]

        # Instantiate some tally Filters
        energy_filter = openmc.EnergyFilter(
            GROUP_STRUCT[self.groups].group_edges)
        mesh_filter = openmc.MeshFilter(mesh)

        # Instantiate the Tally
        tally = openmc.Tally(tally_id=1, name='tally 1')
        tally.filters = [energy_filter, mesh_filter]
        tally.scores = ['flux', 'fission', 'nu-fission']

        # Instantiate a Tallies collection, register all Tallies
        tallies_file = openmc.Tallies([tally])

        return tallies_file

    def make_geometry(self, mats):
        # Instantiate Universe
        root = openmc.Universe(universe_id=0, name='root universe')
        cells = []

        if self.geom == 'IN':
            left = openmc.XPlane(x0=-INF, boundary_type='reflective')
            right = openmc.XPlane(x0=INF, boundary_type='reflective')
            bottom = openmc.YPlane(y0=-INF, boundary_type='reflective')
            top = openmc.YPlane(y0=INF, boundary_type='reflective')
            down = openmc.ZPlane(z0=-INF, boundary_type='reflective')
            up = openmc.ZPlane(z0=INF, boundary_type='reflective')

            # Instantiate Cells
            cells = []
            cells.append(openmc.Cell(name='fissile'))
            yz = (+bottom & -top) & (+down & -up)
            cells[-1].region = (+left & -right) & yz

            # Register Materials with Cells
            cells[-1].fill = mats[0]

        elif self.geom == 'SL':
            surfs = []
            surfs.append(openmc.XPlane(x0=0., boundary_type='reflective'))
            for r, rad in enumerate(self.rad):
                if r == len(self.rad) - 1:
                    surfs.append(openmc.XPlane(x0=rad, boundary_type='vacuum'))
                else:
                    surfs.append(openmc.XPlane(x0=rad))
            bottom = openmc.YPlane(y0=-INF, boundary_type='reflective')
            top = openmc.YPlane(y0=INF, boundary_type='reflective')
            down = openmc.ZPlane(z0=-INF, boundary_type='reflective')
            up = openmc.ZPlane(z0=INF, boundary_type='reflective')

            # Instantiate Cells
            yz = (+bottom & -top) & (+down & -up)
            cells = []
            for c in range(len(surfs) - 1):
                cells.append(openmc.Cell())
                cells[-1].region = (+surfs[c] & -surfs[c + 1]) & yz
                cells[-1].fill = mats[c]

        elif self.geom == 'SL-NS':
            surfs = []
            surfs.append(openmc.XPlane(x0=-self.rad[0],
                                       boundary_type='vacuum'))
            for r, rad in enumerate(self.rad):
                if r == len(self.rad) - 1:
                    surfs.append(openmc.XPlane(x0=rad, boundary_type='vacuum'))
                else:
                    surfs.append(openmc.XPlane(x0=rad))
            bottom = openmc.YPlane(y0=-INF, boundary_type='reflective')
            top = openmc.YPlane(y0=INF, boundary_type='reflective')
            down = openmc.ZPlane(z0=-INF, boundary_type='reflective')
            up = openmc.ZPlane(z0=INF, boundary_type='reflective')

            # Instantiate Cells
            yz = (+bottom & -top) & (+down & -up)
            cells = []
            for c in range(len(surfs) - 1):
                cells.append(openmc.Cell())
                cells[-1].region = (+surfs[c] & -surfs[c + 1]) & yz
                cells[-1].fill = mats[c]

        elif self.geom == 'FENA':
            surfs = []
            surfs.append(openmc.XPlane(x0=0.0, boundary_type='vacuum'))
            for c in range(len(mats) - 1):
                surfs.append(openmc.XPlane(x0=self.rad[c]))
            surfs.append(openmc.XPlane(x0=self.rad[-1],
                                       boundary_type='vacuum'))

            bottom = openmc.YPlane(y0=-INF, boundary_type='reflective')
            top = openmc.YPlane(y0=INF, boundary_type='reflective')
            down = openmc.ZPlane(z0=-INF, boundary_type='reflective')
            up = openmc.ZPlane(z0=INF, boundary_type='reflective')

            # Instantiate Cells
            yz = (+bottom & -top) & (+down & -up)
            cells = []
            for c in range(len(mats)):
                cells.append(openmc.Cell())
                cells[-1].region = (+surfs[c] & -surfs[c + 1]) & yz
                cells[-1].fill = mats[c]

        elif self.geom == 'CY':
            surfs = []
            for r, rad in enumerate(self.rad):
                if r == len(self.rad) - 1:
                    surfs.append(openmc.ZCylinder(R=rad,
                                                  boundary_type='vacuum'))
                else:
                    surfs.append(openmc.ZCylinder(R=rad))

            # Instantiate Cells
            cells = []
            cells.append(openmc.Cell())
            cells[-1].region = -surfs[0]
            cells[-1].fill = mats[0]
            for c in range(1, len(surfs)):
                cells.append(openmc.Cell())
                cells[-1].region = (+surfs[c - 1] & -surfs[c])
                cells[-1].fill = mats[c]

        elif self.geom == 'SP':
            surfs = []
            for r, rad in enumerate(self.rad):
                if r == len(self.rad) - 1:
                    surfs.append(openmc.Sphere(R=rad, boundary_type='vacuum'))
                else:
                    surfs.append(openmc.Sphere(R=rad))

            # Instantiate Cells
            cells = []
            cells.append(openmc.Cell())
            cells[-1].region = -surfs[0]
            cells[-1].fill = mats[0]
            for c in range(1, len(surfs)):
                cells.append(openmc.Cell())
                cells[-1].region = (+surfs[c - 1] & -surfs[c])
                cells[-1].fill = mats[c]

        elif self.geom == 'ISLC':
            surfs = []
            surfs.append(openmc.XPlane(x0=0., boundary_type='reflective'))
            for r, rad in enumerate(self.rad):
                if r == len(self.rad) - 1:
                    surfs.append(openmc.XPlane(x0=rad,
                                               boundary_type='reflective'))
                else:
                    surfs.append(openmc.XPlane(x0=rad))
            bottom = openmc.YPlane(y0=-INF, boundary_type='reflective')
            top = openmc.YPlane(y0=INF, boundary_type='reflective')
            down = openmc.ZPlane(z0=-INF, boundary_type='reflective')
            up = openmc.ZPlane(z0=INF, boundary_type='reflective')

            # Instantiate Cells
            yz = (+bottom & -top) & (+down & -up)
            cells = []
            for c in range(len(surfs) - 1):
                cells.append(openmc.Cell())
                cells[-1].region = (+surfs[c] & -surfs[c + 1]) & yz
                cells[-1].fill = mats[c]

        # Register Cells with Universe
        root.add_cells(cells)

        # Instantiate a Geometry, register the root Universe, and export to XML
        geometry = openmc.Geometry(root)

        return geometry

    def make_model(self):
        mats, materials_file = self.make_materials()
        materials_file.export_to_xml()

        settings_file = self.make_settings()
        settings_file.export_to_xml()

        tallies_file = self.make_tallies(r=np.max(self.rad))
        if tallies_file:
            tallies_file.export_to_xml()

        geometry = self.make_geometry(mats)
        geometry.export_to_xml()

    def execute(self, quiet=True):
        returncode = openmc.run(output=(not quiet))
        spfile = 'statepoint.' + str(self.batches) + '.h5'
        sp = openmc.StatePoint(spfile, autolink=False)
        self.keff = sp.k_combined

        return returncode
