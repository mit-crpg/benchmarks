import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('g/cm3', 15.9)
mat.add_nuclide('Pu239', 0.037592)
mat.add_nuclide('Pu240', 0.0019349)
mat.add_nuclide('Pu241', 0.00011797)
mat.add_nuclide('Ga69', 0.000825463164)
mat.add_nuclide('Ga71', 0.000547836836)
mats.append(mat)

mat = openmc.Material(2)
mat.set_density('g/cm3', 2.82)
mat.add_nuclide('Al27', 0.058787)
mat.add_nuclide('Cu63', 0.00081337003)
mat.add_nuclide('Cu65', 0.00036252997)
mat.add_nuclide('Si28', 0.00022307597539)
mat.add_nuclide('Si39', 1.1327134905e-05)
mat.add_nuclide('Si30', 7.466889705e-06)
mat.add_nuclide('Mn55', 0.00024729)
mat.add_nuclide('Mg24', 0.000275959464)
mat.add_nuclide('Mg25', 3.4936e-05)
mat.add_nuclide('Mg26', 3.8464536e-05)
mats.append(mat)

mats.export_to_xml()