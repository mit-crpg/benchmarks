import openmc
from openmc.source import Source
from openmc.stats import Box
import sys
sys.path.append('../')
from lattices import lattices, universes, cells, surfaces
from tally import tallies, mesh

###############################################################################
#                      Simulation Input File Parameters
###############################################################################

# OpenMC simulation parameters
batches = 20000
inactive = 500
particles = 10000


###############################################################################
#                 Exporting to OpenMC materials.xml File
###############################################################################

from materials import materials

# Instantiate a MaterialsFile, register all Materials, and export to XML
materials_file = openmc.MaterialsFile()
materials_file.default_xs = '300k'
materials_file.add_materials(materials.values())
materials_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC geometry.xml File
###############################################################################

# Instantiate Core boundaries
cells['Core'].region = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                       +surfaces['Small Core z-min'] & -surfaces['Core x-max'] & \
                       -surfaces['Core y-max'] & -surfaces['Small Core z-max']

lattices['Core'] = openmc.RectLattice(lattice_id=201, name='3x3 core lattice')
lattices['Core'].dimension = [3,3,9]
lattices['Core'].lower_left = [-32.13, -32.13, -32.13]
lattices['Core'].pitch = [21.42, 21.42, 7.14]
w = universes['Reflector Unrodded Assembly']
x = universes['Reflector Rodded Assembly']
u = universes['UO2 Unrodded Assembly']
v = universes['UO2 Rodded Assembly']
m = universes['MOX Unrodded Assembly']
n = universes['MOX Rodded Assembly']
lattices['Core'].universes = [[[u, m, w], [m, u, w], [w, w, w]]] * 6 + \
                             [[[x, x, w], [x, x, w], [w, w, w]]] * 3

# Add Core lattice to Core cell
cells['Core'].fill = lattices['Core']

# Instantiate a Geometry and register the root Universe
geometry = openmc.Geometry()
geometry.root_universe = universes['Root']

# Instantiate a GeometryFile, register Geometry, and export to XML
geometry_file = openmc.GeometryFile()
geometry_file.geometry = geometry
geometry_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC settings.xml File
###############################################################################

# Instantiate a SettingsFile, set all runtime parameters, and export to XML
settings_file = openmc.SettingsFile()
settings_file.energy_mode = "multi-group"
settings_file.cross_sections = "./mg_cross_sections.xml"
settings_file.batches = batches
settings_file.inactive = inactive
settings_file.particles = particles
settings_file.output = {'tallies': True, 'summary': True}
settings_file.source = Source(space=Box([-32.13, -10.71, -107.1], [10.71, 32.13, 85.68]))
settings_file.entropy_lower_left = [-32.13, -32.13, -107.1]
settings_file.entropy_upper_right = [32.13,  32.13,  107.1]
settings_file.entropy_dimension = [51, 51, 30]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC plots.xml File
###############################################################################

plot_1 = openmc.Plot(plot_id=1)
plot_1.filename = 'plot_1'
plot_1.origin = [0.0, 0.0, 0.0]
plot_1.width = [64.26, 64.26]
plot_1.pixels = [500, 500]
plot_1.color = 'mat'
plot_1.basis = 'xy'

plot_2 = openmc.Plot(plot_id=2)
plot_2.filename = 'plot_2'
plot_2.origin = [0.0, 21.42, 0.0]
plot_2.width = [64.26, 64.26]
plot_2.pixels = [500, 500]
plot_2.color = 'mat'
plot_2.basis = 'xz'

# Instantiate a PlotsFile, add Plot, and export to XML
plot_file = openmc.PlotsFile()
plot_file.add_plot(plot_1)
plot_file.add_plot(plot_2)
plot_file.export_to_xml()

###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################

# Instantiate a TalliesFile, register Tally/Mesh, and export to XML
tallies_file = openmc.TalliesFile()
tallies_file.add_mesh(mesh)

for tally in tallies.values():
    tallies_file.add_tally(tally)

tallies_file.export_to_xml()
