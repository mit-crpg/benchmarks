import openmc
from openmc.source import Source
from openmc.stats import Box
import sys
sys.path.append('../')
import cells

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
universes = {}
universes['Root'] = openmc.Universe(universe_id=0,  name='Root')
universes['Root'].add_cells([cells.cells['UO2'], cells.cells['UO2 Pin']])

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
settings_file.source = Source(space=Box([-0.63,-0.63,-1.E50],
                                        [ 0.63, 0.63, 1.E50],
                                        only_fissionable=True))
settings_file.entropy_lower_left  = [-0.63,-0.63,-1.E50]
settings_file.entropy_upper_right = [ 0.63, 0.63, 1.E50]
settings_file.entropy_dimension = [10,10,1]
settings_file.export_to_xml()


###############################################################################
#                   Exporting to OpenMC plots.xml File
###############################################################################

plot_1 = openmc.Plot(plot_id=1)
plot_1.filename = 'plot_1'
plot_1.origin = [0.0, 0.0, 0.0]
plot_1.width = [1.26, 1.26]
plot_1.pixels = [500, 500]
plot_1.color = 'mat'
plot_1.basis = 'xy'

# Instantiate a PlotsFile, add Plot, and export to XML
plot_file = openmc.PlotsFile()
plot_file.add_plot(plot_1)
plot_file.export_to_xml()

###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################


tallies = {}

# Instantiate a tally mesh
mesh = openmc.Mesh(mesh_id=1)
mesh.type = 'regular'
mesh.dimension = [51, 51, 1]
mesh.lower_left  = [-0.63,-0.63,-1.e50]
mesh.upper_right = [ 0.63, 0.63, 1.e50]

# Instantiate some tally Filters
mesh_filter = openmc.Filter()
mesh_filter.mesh = mesh

# Instantiate the Tally
tallies['Mesh Rates'] = openmc.Tally(tally_id=1, name='tally 1')
tallies['Mesh Rates'].add_filter(mesh_filter)
tallies['Mesh Rates'].add_score('flux')
tallies['Mesh Rates'].add_score('fission')
tallies['Mesh Rates'].add_score('nu-fission')

tallies['Global Rates'] = openmc.Tally(tally_id=2, name='tally 2')
tallies['Global Rates'].add_score('flux')
tallies['Global Rates'].add_score('fission')
tallies['Global Rates'].add_score('nu-fission')

# Instantiate a TalliesFile, register Tally/Mesh, and export to XML
tallies_file = openmc.TalliesFile()
tallies_file.add_mesh(mesh)

for tally in tallies.values():
    tallies_file.add_tally(tally)

tallies_file.export_to_xml()
