import openmc
import openmc.mgxs
import numpy as np
from universes import universes, cells, surfaces

###############################################################################
#                     Create a dictionary of the assembly lattices
###############################################################################

# Instantiate the Lattices
lattices = {}
lattices['UO2 Unrodded Assembly'] = openmc.RectLattice(lattice_id=101, name='UO2 Unrodded Assembly')
lattices['UO2 Unrodded Assembly'].dimension = [17, 17]
lattices['UO2 Unrodded Assembly'].lower_left = [-10.71, -10.71]
lattices['UO2 Unrodded Assembly'].pitch = [1.26, 1.26]
u = universes['UO2']
g = universes['Guide Tube']
f = universes['Fission Chamber']
lattices['UO2 Unrodded Assembly'].universes = [[u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, u, u, u, g, u, u, g, u, u, g, u, u, u, u, u],
                                               [u, u, u, g, u, u, u, u, u, u, u, u, u, g, u, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, g, u, u, g, u, u, g, u, u, g, u, u, g, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, g, u, u, g, u, u, f, u, u, g, u, u, g, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, g, u, u, g, u, u, g, u, u, g, u, u, g, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, u, g, u, u, u, u, u, u, u, u, u, g, u, u, u],
                                               [u, u, u, u, u, g, u, u, g, u, u, g, u, u, u, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                               [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]]

lattices['UO2 Rodded Assembly'] = openmc.RectLattice(lattice_id=102, name='UO2 Rodded Assembly')
lattices['UO2 Rodded Assembly'].dimension = [17, 17]
lattices['UO2 Rodded Assembly'].lower_left = [-10.71, -10.71]
lattices['UO2 Rodded Assembly'].pitch = [1.26, 1.26]
u = universes['UO2']
r = universes['Control Rod']
f = universes['Fission Chamber']
lattices['UO2 Rodded Assembly'].universes = [[u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
                                             [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, r, u, u, r, u, u, f, u, u, r, u, u, r, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
                                             [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                             [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]]

lattices['MOX Unrodded Assembly'] = openmc.RectLattice(lattice_id=103, name='MOX Unrodded Assembly')
lattices['MOX Unrodded Assembly'].dimension = [17, 17]
lattices['MOX Unrodded Assembly'].lower_left = [-10.71, -10.71]
lattices['MOX Unrodded Assembly'].pitch = [1.26, 1.26]
m = universes['MOX 4.3%']
n = universes['MOX 7.0%']
o = universes['MOX 8.7%']
g = universes['Guide Tube']
f = universes['Fission Chamber']
lattices['MOX Unrodded Assembly'].universes = [[m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                               [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
                                               [m, n, n, n, n, g, n, n, g, n, n, g, n, n, n, n, m],
                                               [m, n, n, g, n, o, o, o, o, o, o, o, n, g, n, n, m],
                                               [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
                                               [m, n, g, o, o, g, o, o, g, o, o, g, o, o, g, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, g, o, o, g, o, o, f, o, o, g, o, o, g, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, g, o, o, g, o, o, g, o, o, g, o, o, g, n, m],
                                               [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
                                               [m, n, n, g, n, o, o, o, o, o, o, o, n, g, n, n, m],
                                               [m, n, n, n, n, g, n, n, g, n, n, g, n, n, n, n, m],
                                               [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
                                               [m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]]

lattices['MOX Rodded Assembly'] = openmc.RectLattice(lattice_id=104, name='MOX Rodded Assembly')
lattices['MOX Rodded Assembly'].dimension = [17, 17]
lattices['MOX Rodded Assembly'].lower_left = [-10.71, -10.71]
lattices['MOX Rodded Assembly'].pitch = [1.26, 1.26]
m = universes['MOX 4.3%']
n = universes['MOX 7.0%']
o = universes['MOX 8.7%']
r = universes['Control Rod']
f = universes['Fission Chamber']
lattices['MOX Rodded Assembly'].universes = [[m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m],
                                               [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
                                               [m, n, n, n, n, r, n, n, r, n, n, r, n, n, n, n, m],
                                               [m, n, n, r, n, o, o, o, o, o, o, o, n, r, n, n, m],
                                               [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
                                               [m, n, r, o, o, r, o, o, r, o, o, r, o, o, r, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, r, o, o, r, o, o, f, o, o, r, o, o, r, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, n, o, o, o, o, o, o, o, o, o, o, o, n, n, m],
                                               [m, n, r, o, o, r, o, o, r, o, o, r, o, o, r, n, m],
                                               [m, n, n, n, o, o, o, o, o, o, o, o, o, n, n, n, m],
                                               [m, n, n, r, n, o, o, o, o, o, o, o, n, r, n, n, m],
                                               [m, n, n, n, n, r, n, n, r, n, n, r, n, n, n, n, m],
                                               [m, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, m],
                                               [m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m]]

lattices['Reflector Unrodded Assembly'] = openmc.RectLattice(lattice_id=105, name='Reflector Unrodded Assembly')
lattices['Reflector Unrodded Assembly'].dimension = [1,1]
lattices['Reflector Unrodded Assembly'].lower_left = [-10.71, -10.71]
lattices['Reflector Unrodded Assembly'].pitch = [21.42, 21.42]
w = universes['Reflector']
lattices['Reflector Unrodded Assembly'].universes = [[w]]

lattices['Reflector Rodded Assembly'] = openmc.RectLattice(lattice_id=106, name='Reflector Rodded Assembly')
lattices['Reflector Rodded Assembly'].dimension = [17, 17]
lattices['Reflector Rodded Assembly'].lower_left = [-10.71, -10.71]
lattices['Reflector Rodded Assembly'].pitch = [1.26, 1.26]
u = universes['Reflector']
r = universes['Control Rod']
lattices['Reflector Rodded Assembly'].universes = [[u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
                                                   [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, r, u, u, r, u, u, u, u, u, r, u, u, r, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, r, u, u, r, u, u, r, u, u, r, u, u, r, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, u, r, u, u, u, u, u, u, u, u, u, r, u, u, u],
                                                   [u, u, u, u, u, r, u, u, r, u, u, r, u, u, u, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
                                                   [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]]

# Add lattice to cells
cells['UO2 Unrodded Assembly'].fill       = lattices['UO2 Unrodded Assembly']
cells['UO2 Rodded Assembly'].fill         = lattices['UO2 Rodded Assembly']
cells['MOX Unrodded Assembly'].fill       = lattices['MOX Unrodded Assembly']
cells['MOX Rodded Assembly'].fill         = lattices['MOX Rodded Assembly']
cells['Reflector Unrodded Assembly'].fill = lattices['Reflector Unrodded Assembly']
cells['Reflector Rodded Assembly'].fill   = lattices['Reflector Rodded Assembly']
