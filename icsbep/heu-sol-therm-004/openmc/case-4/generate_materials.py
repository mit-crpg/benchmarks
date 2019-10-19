import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "UO2F2/D2O Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 5.1847e-06)
mat.add_nuclide('U235', 4.7399e-04)
mat.add_nuclide('U238', 2.6636e-05)
mat.add_nuclide('F19', 1.0116e-03)
mat.add_element('O', 3.3077e-02)
mat.add_nuclide('H2', 6.3939e-02)
mat.add_nuclide('H1', 1.9239e-04)
mat.add_s_alpha_beta('c_D_in_D2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "321 Stainless Steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9355e-02)
mat.add_element('Cr', 1.6511e-02)
mat.add_element('Ni', 7.7203e-03)
mat.add_element('Mn', 1.7363e-03)
mat.add_element('Si', 1.6982e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Heavy Water"
mat.set_density('sum')
mat.add_nuclide('H2', 6.6078e-02)
mat.add_nuclide('H1', 3.9886e-04)
mat.add_element('O', 3.3238e-02)
mat.add_s_alpha_beta('c_D_in_D2O')
mats.append(mat)

mats.export_to_xml()
