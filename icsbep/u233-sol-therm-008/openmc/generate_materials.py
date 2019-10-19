import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "UO2(NO3)2 Solution"
mat.set_density('sum')
mat.add_nuclide('U233', 3.3441e-05)
mat.add_nuclide('U234', 5.2503e-07)
mat.add_nuclide('U235', 1.0184e-08)
mat.add_nuclide('U238', 2.5474e-07)
mat.add_nuclide('N14', 7.4943e-05)
mat.add_nuclide('H1', 6.6357e-02)
mat.add_element('O', 3.3469e-02)
mat.add_nuclide('Th232', 1.4756e-07)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Type 1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9881e-02)
mat.add_element('Si', 2.1790e-04)
mat.add_element('Fe', 1.0958e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mats.export_to_xml()
