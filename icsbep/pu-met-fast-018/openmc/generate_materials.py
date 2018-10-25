import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.7291e-02)
mat.add_nuclide('Pu240', 1.9277e-03)
mat.add_nuclide('Pu241', 1.2196e-04)
mat.add_element('Ga', 1.3628e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.set_density('sum')
mat.add_element('Be', 1.1984e-01)
mat.add_element('O', 1.3776e-03)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mats.export_to_xml()
