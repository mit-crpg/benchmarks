"""
Description: Topsy Reflected Oralloy Spherical Assembly
Case:        HEU-MET-FAST-003 1.9-in WC reflector
"""

import openmc

oralloy = openmc.Material(name="Oralloy")
oralloy.add_nuclide('U234', 4.9210e-04)
oralloy.add_nuclide('U235', 4.4917e-02)
oralloy.add_nuclide('U238', 2.5993e-03)

wc = openmc.Material(name="Tungsten carbide")
wc.add_nuclide('W182', 1.2697e-02)
wc.add_nuclide('W183', 6.8626e-03)
wc.add_nuclide('W184', 1.4754e-02)
wc.add_nuclide('W186', 1.3744e-02)
wc.add_element('C', 4.8057e-02)

materials = openmc.Materials([oralloy, wc])
materials.export_to_xml()
