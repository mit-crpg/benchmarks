import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 9.4068e-06)
mat.add_nuclide('U235', 8.5392e-04)
mat.add_nuclide('U236', 3.9607e-06)
mat.add_nuclide('U238', 4.8613e-05)
mat.add_element('O', 3.7252e-02)
mat.add_nuclide('N14', 2.1624e-03)
mat.add_nuclide('H1', 5.8196e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Aluminum Tank"
mat.set_density('sum')
mat.add_nuclide('Al27', 5.9469e-02)
mats.append(mat)

mats.export_to_xml()
