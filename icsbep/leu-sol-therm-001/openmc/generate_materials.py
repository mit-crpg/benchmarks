import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "SS304L"
mat.set_density('sum')
mat.add_element('Cr', 1.6348e-02)
mat.add_element('Mn', 1.7192e-03)
mat.add_element('Fe', 6.0038e-02)
mat.add_element('Ni', 7.2418e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Air"
mat.set_density('sum')
mat.add_element('N', 3.5214e-05)
mat.add_element('O', 1.5092e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Fuel Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 6.7855e-07)
mat.add_nuclide('U235', 1.2377e-04)
mat.add_nuclide('U236', 1.2085e-06)
mat.add_nuclide('U238', 2.3508e-03)
mat.add_nuclide('H1', 5.6179e-02)
mat.add_element('O', 3.2967e-02)
mat.add_element('F', 5.1035e-03)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
