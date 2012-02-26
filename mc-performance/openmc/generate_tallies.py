#!/usr/bin/env python

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

# Open tallies.xml file
fh = open('tallies.xml','w')

# Write header tags
fh.write('<?xml version="1.0"?>\n<tallies>\n\n')

# Write meshes and assemblies
for i, assem in enumerate(assemblies):
    x, y = assem
    fh.write('  <mesh id="{0}">\n'.format(i+1))
    fh.write('    <type>rectangular</type>\n')
    fh.write('    <lower_left>{0} {1}</lower_left>\n'.format(
            -182.07 + 21.42*(x-1), -182.07 + 21.42*(y-1)))
    fh.write('    <width>1.26 1.26</width>\n')
    fh.write('    <dimension>17 17</dimension>\n')
    fh.write('  </mesh>\n')
    fh.write('  <tally id="{0}">\n'.format(i+1))
    fh.write('    <filters>\n')
    fh.write('      <mesh>{0}</mesh>\n'.format(i+1))
    fh.write('    </filters>\n')
    fh.write('    <scores>nu-fission</scores>\n')
    fh.write('  </tally>\n\n')

# Write closing tags
fh.write('</tallies>\n')
