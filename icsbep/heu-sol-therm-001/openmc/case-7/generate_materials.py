import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 3.6132e-06)
mat.add_nuclide('U235', 3.2800e-04)
mat.add_nuclide('U236', 1.5214e-06)
mat.add_nuclide('U238', 1.8673e-05)
mat.add_element('O', 3.4945e-02)
mat.add_nuclide('N14', 8.7645e-04)
mat.add_nuclide('H1', 6.3397e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Aluminum Tank"
mat.set_density('sum')
mat.add_nuclide('Al27', 5.9469e-02)
mats.append(mat)

mats.export_to_xml()
