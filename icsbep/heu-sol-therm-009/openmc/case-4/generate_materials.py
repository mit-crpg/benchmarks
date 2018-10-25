import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranium Oxyfluoride Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 5.3760e-06)
mat.add_nuclide('U235', 5.0898e-04)
mat.add_nuclide('U236', 2.7195e-06)
mat.add_nuclide('U238', 2.8800e-05)
mat.add_nuclide('F19', 1.0917e-03)
mat.add_element('O', 3.3278e-02)
mat.add_nuclide('H1', 6.4373e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9699e-02)
mat.add_element('Si', 5.5202e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water Reflector at 25 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6659e-02)
mat.add_element('O', 3.3329e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
