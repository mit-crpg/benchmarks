import openmc

###############################################################################
#                   Exporting to OpenMC tallies.xml File
###############################################################################

tallies = {}

# Instantiate a tally mesh
mesh = openmc.Mesh(mesh_id=1)
mesh.type = 'regular'
mesh.dimension = [51, 51, 1]
mesh.lower_left = [-32.13, -32.13, -1.e50]
mesh.upper_right = [32.13, 32.13, 1.e50]

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
