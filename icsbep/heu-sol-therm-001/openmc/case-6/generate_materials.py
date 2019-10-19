import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5686e-06)
mat.add_nuclide('U235', 1.4240e-04)
mat.add_nuclide('U236', 6.6047e-07)
mat.add_nuclide('U238', 8.1064e-06)
mat.add_element('O', 3.4057e-02)
mat.add_nuclide('N14', 3.7412e-04)
mat.add_nuclide('H1', 6.5327e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Aluminum Tank"
mat.set_density('sum')
mat.add_nuclide('Al27', 5.9469e-02)
mats.append(mat)

mats.export_to_xml()
