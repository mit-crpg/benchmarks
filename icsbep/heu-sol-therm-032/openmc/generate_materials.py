import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranium Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U233', 3.9124e-09)
mat.add_nuclide('U234', 4.0905e-07)
mat.add_nuclide('U235', 3.6157e-05)
mat.add_nuclide('U236', 2.0858e-07)
mat.add_nuclide('U238', 1.9878e-06)
mat.add_nuclide('N14', 1.1212e-04)
mat.add_nuclide('H1', 6.6409e-02)
mat.add_element('O', 3.3601e-02)
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
