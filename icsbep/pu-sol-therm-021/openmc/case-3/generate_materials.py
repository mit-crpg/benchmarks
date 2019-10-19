import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 2.6153e-08)
mat.add_nuclide('Pu239', 4.1249e-04)
mat.add_nuclide('Pu240', 2.0181e-05)
mat.add_nuclide('Pu241', 1.2181e-06)
mat.add_nuclide('Pu242', 3.8579e-08)
mat.add_nuclide('N14', 4.6867e-03)
mat.add_nuclide('H1', 5.4377e-02)
mat.add_nuclide('O16', 3.9773e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "304L Stainless Steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9355e-02)
mat.add_element('Cr', 1.7428e-02)
mat.add_element('Ni', 7.7203e-03)
mat.add_element('Mn', 1.7363e-03)
mats.append(mat)

mats.export_to_xml()
