import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Pu core"
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.5536e-02)
mat.add_nuclide('Pu240', 2.7719e-03)
mat.add_nuclide('Pu241', 1.7313e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U235', 4.4401e-02)
mat.add_nuclide('U238', 3.2137e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Beryllium"
mat.set_density('sum')
mat.add_element('Be', 1.2295e-01)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mats.export_to_xml()
