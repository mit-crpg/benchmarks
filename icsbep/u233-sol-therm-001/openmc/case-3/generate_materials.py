import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "UO2(NO3)2 Solution"
mat.set_density('sum')
mat.add_nuclide('U233', 4.6768e-05)
mat.add_nuclide('U234', 7.7216e-07)
mat.add_nuclide('U235', 1.8984e-08)
mat.add_nuclide('U238', 2.9991e-07)
mat.add_nuclide('N14', 1.2772e-04)
mat.add_nuclide('H1', 6.6413e-02)
mat.add_element('O', 3.3674e-02)
mat.add_nuclide('B10', 5.1591e-07)
mat.add_nuclide('B11', 2.0766e-06)
mat.add_nuclide('Th232', 2.1331e-07)
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
