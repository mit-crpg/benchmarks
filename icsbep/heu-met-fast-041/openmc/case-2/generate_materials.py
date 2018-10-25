import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 4.8817e-04)
mat.add_nuclide('U235', 4.4605e-02)
mat.add_nuclide('U238', 2.5315e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Beryllium"
mat.set_density('sum')
mat.add_element('Be', 1.2295e-01)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mats.export_to_xml()
