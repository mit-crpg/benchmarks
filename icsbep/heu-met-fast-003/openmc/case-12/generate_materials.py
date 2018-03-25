import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Oralloy"
mat.set_density('sum')
mat.add_nuclide('U234', 4.9210e-4)
mat.add_nuclide('U235', 4.4917e-2)
mat.add_nuclide('U238', 2.5993e-3)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Nickel"
mat.set_density('sum')
mat.add_element('Ni', 9.1322e-02)
mats.append(mat)

mats.export_to_xml()
