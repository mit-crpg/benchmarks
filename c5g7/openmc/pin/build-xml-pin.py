import openmc
import sys
sys.path.append('../')
import cells
from materials import materials


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

# Instantiate a Materials, register all Materials, and export to XML
materials_file = openmc.Materials(materials.values())
materials_file.cross_sections = './mgxs.h5'
materials_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC geometry.xml File
###############################################################################

# Instantiate Core boundaries
universes = {}
universes['Root'] = openmc.Universe(universe_id=0,  name='Root')
universes['Root'].add_cells([cells.cells['UO2'], cells.cells['UO2 Pin']])

# Instantiate a Geometry, register the root Universe, and export to XML
geometry = openmc.Geometry()
geometry.root_universe = universes['Root']
geometry.export_to_xml()


###############################################################################
#                   Exporting to OpenMC settings.xml File
###############################################################################

# Instantiate a Settings, set all runtime parameters, and export to XML
settings_file = openmc.Settings()
settings_file.energy_mode = "multi-group"
settings_file.batches = batches
settings_file.inactive = inactive
settings_file.particles = particles
settings_file.output = {'tallies': True, 'summary': True}
settings_file.source = openmc.Source(space=openmc.stats.Box(
    [-0.63, -0.63, -1.e50], [0.63, 0.63, 1.e50], only_fissionable=True))
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
plot_1.color_by = 'material'
plot_1.basis = 'xy'

# Instantiate a Plots collection and export to XML
plot_file = openmc.Plots([plot_1])
plot_file.export_to_xml()

###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################


tallies = {}

# Instantiate a tally mesh
mesh = openmc.RegularMesh(mesh_id=1)
mesh.dimension = [51, 51, 1]
mesh.lower_left  = [-0.63,-0.63,-1.e50]
mesh.upper_right = [ 0.63, 0.63, 1.e50]

# Instantiate some tally Filters
mesh_filter = openmc.MeshFilter(mesh)

# Instantiate the Tally
tallies['Mesh Rates'] = openmc.Tally(tally_id=1, name='tally 1')
tallies['Mesh Rates'].filters = [mesh_filter]
tallies['Mesh Rates'].scores = ['flux', 'fission', 'nu-fission']

tallies['Global Rates'] = openmc.Tally(tally_id=2, name='tally 2')
tallies['Global Rates'].scores = ['flux', 'fission', 'nu-fission']

# Instantiate a Tallies collection and export to XML
tallies_file = openmc.Tallies(tallies.values())
tallies_file.export_to_xml()
