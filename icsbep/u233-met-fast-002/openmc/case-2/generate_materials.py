import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "U-233 Inner Sphere"
mat.set_density('g/cm3', 18.644)
mat.add_nuclide('U233', 0.047312)
mat.add_nuclide('U235', 0.00052707)
mat.add_nuclide('U238', 0.00033015)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "U-235 Outer Shell"
mat.set_density('g/cm3', 18.8)
mat.add_nuclide('U235', 0.044892)
mat.add_nuclide('U238', 0.003234)
mats.append(mat)

mats.export_to_xml()