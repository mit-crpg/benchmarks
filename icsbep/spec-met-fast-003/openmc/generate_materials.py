import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Np237', 5.1876e-2)
mats.append(mat)

mat = openmc.Material(2)
mat.set_density('sum')
mat.add_element('Ni', 9.1322e-2)
mats.append(mat)

mat = openmc.Material(3)
mat.set_density('sum')
mat.add_nuclide('U234', 4.8869e-4)
mat.add_nuclide('U235', 4.4482e-2)
mat.add_nuclide('U238', 2.7038e-3)
mats.append(mat)

mat = openmc.Material(4)
mat.set_density('sum')
mat.add_nuclide('U235', 3.5050e-4)
mat.add_nuclide('U238', 4.7717e-2)
mats.append(mat)

mats.export_to_xml()
