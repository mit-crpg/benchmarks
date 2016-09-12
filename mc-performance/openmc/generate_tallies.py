#!/usr/bin/env python

import openmc

# Set up list of assembly positions
assemblies = ([(1,i) for i in range(6,13)] +
              [(2,i) for i in range(4,15)] +
              [(3,i) for i in range(3,16)] +
              [(4,i) for i in range(2,17)] +
              [(5,i) for i in range(2,17)] +
              [(6,i) for i in range(1,18)] +
              [(7,i) for i in range(1,18)] +
              [(8,i) for i in range(1,18)] +
              [(9,i) for i in range(1,18)] +
              [(10,i) for i in range(1,18)] +
              [(11,i) for i in range(1,18)] +
              [(12,i) for i in range(1,18)] +
              [(13,i) for i in range(2,17)] +
              [(14,i) for i in range(2,17)] +
              [(15,i) for i in range(3,16)] +
              [(16,i) for i in range(4,15)] +
              [(17,i) for i in range(6,13)])

# Write meshes and assemblies
tallies = openmc.Tallies()
for i, assem in enumerate(assemblies):
    x, y = assem
    mesh = openmc.Mesh()
    mesh.lower_left = (-182.07 + 21.42*(x-1), -182.07 + 21.42*(y-1))
    mesh.width = (1.26, 1.26)
    mesh.dimension = (17, 17)

    tally = openmc.Tally()
    tally.filters = [openmc.MeshFilter(mesh)]
    tally.nuclides = ['all']
    tally.scores = ['total']
    tallies.append(tally)

tallies.export_to_xml()
