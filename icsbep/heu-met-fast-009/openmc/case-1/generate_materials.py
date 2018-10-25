import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2195e-04)
mat.add_nuclide('U235', 4.1000e-02)
mat.add_nuclide('U236', 8.8422e-05)
mat.add_nuclide('U238', 4.0977e-03)
mat.add_element('C', 3.9932e-04)
mat.add_element('Fe', 1.3531e-04)
mat.add_element('W', 1.2445e-05)
mat.add_element('Cu', 7.3334e-04)
mat.add_element('Ni', 3.4029e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Be Reflector"
mat.set_density('sum')
mat.add_element('Be', 1.2080e-01)
mat.add_element('O', 8.2053e-05)
mat.add_element('C', 1.0019e-04)
mat.add_element('Fe', 5.0932e-05)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Fe"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Copper"
mat.set_density('sum')
mat.add_element('Cu', 8.2365e-02)
mats.append(mat)

mats.export_to_xml()
