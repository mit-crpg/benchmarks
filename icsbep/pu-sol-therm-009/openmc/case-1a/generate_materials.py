import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 1.0139e-09)
mat.add_nuclide('Pu239', 2.4582e-05)
mat.add_nuclide('Pu240', 6.3369e-07)
mat.add_nuclide('Pu241', 1.8774e-08)
mat.add_nuclide('Pu242', 3.4900e-09)
mat.add_nuclide('N14', 7.6339e-04)
mat.add_nuclide('H1', 6.5198e-02)
mat.add_nuclide('O16', 3.4558e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9881e-02)
mat.add_element('Si', 3.7770e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mats.export_to_xml()
