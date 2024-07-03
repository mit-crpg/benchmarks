"""
Description: Topsy Reflected Oralloy Spherical Assembly
Case:        HEU-MET-FAST-003 8-in Tuballoy reflector
"""

import openmc

oralloy = openmc.Material(name="Oralloy")
oralloy.add_nuclide('U234', 4.9210e-04)
oralloy.add_nuclide('U235', 4.4917e-02)
oralloy.add_nuclide('U238', 2.5993e-03)

tuballoy = openmc.Material(name="Tuballoy")
tuballoy.add_nuclide('U234', 2.6299e-06)
tuballoy.add_nuclide('U235', 3.4428e-04)
tuballoy.add_nuclide('U238', 4.7470e-02)

materials = openmc.Materials([oralloy, tuballoy])
materials.export_to_xml()
