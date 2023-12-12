import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Oralloy"
mat.set_density('g/cm3', 18.75)
mat.add_nuclide('U234', 0.0004921)
mat.add_nuclide('U235', 0.044917)
mat.add_nuclide('U238', 0.0025993)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Tuballoy"
mat.set_density('g/cm3', 18.90)
mat.add_nuclide('U234', 2.6299e-06)
mat.add_nuclide('U235', 0.00034428)
mat.add_nuclide('U238', 0.04747)
mats.append(mat)

mats.export_to_xml()
