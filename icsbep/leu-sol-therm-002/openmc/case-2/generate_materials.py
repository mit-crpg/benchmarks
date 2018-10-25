import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranium Oxyfluoride Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 2.5304e-07)
mat.add_nuclide('U235', 6.1604e-05)
mat.add_nuclide('U238', 1.1828e-03)
mat.add_element('F', 2.4893e-03)
mat.add_element('O', 3.3331e-02)
mat.add_nuclide('H1', 6.1683e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Type 1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9699e-02)
mat.add_element('Si', 5.5202e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mats.export_to_xml()
