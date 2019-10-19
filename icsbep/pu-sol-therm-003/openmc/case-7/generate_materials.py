import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu239', 8.7811e-05)
mat.add_nuclide('Pu240', 2.8161e-06)
mat.add_nuclide('N14', 9.0422e-04)
mat.add_nuclide('H1', 6.4783e-02)
mat.add_nuclide('O16', 3.4833e-02)
mat.add_element('Fe', 1.2293e-06)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "2S (1100) aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9881e-02)
mat.add_element('Si', 3.7770e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 27 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6622e-02)
mat.add_nuclide('O16', 3.3311e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
