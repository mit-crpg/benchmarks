import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "UO2F2/D2O Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 8.4636e-06)
mat.add_nuclide('U235', 7.7376e-04)
mat.add_nuclide('U238', 4.3482e-05)
mat.add_nuclide('F19', 1.6514e-03)
mat.add_element('O', 3.3066e-02)
mat.add_nuclide('H2', 6.2641e-02)
mat.add_nuclide('H1', 1.8849e-04)
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
