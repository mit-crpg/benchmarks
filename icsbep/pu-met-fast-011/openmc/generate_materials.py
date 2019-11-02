import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.6982e-02)
mat.add_nuclide('Pu240', 2.5852e-03)
mat.add_nuclide('Pu241', 1.4915e-04)
mat.add_nuclide('Pu242', 9.9432e-06)
mats.append(mat)

mat = openmc.Material(2)
mat.set_density('sum')
mat.add_nuclide('H1', 6.6766e-02)
mat.add_element('O', 3.3383e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
