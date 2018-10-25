import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Beryllium (internal)"
mat.set_density('sum')
mat.add_element('Be', 1.1862e-01)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Nickel"
mat.set_density('sum')
mat.add_element('Ni', 9.1290e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Air"
mat.set_density('sum')
mat.add_element('N', 3.8595e-05)
mat.add_element('O', 1.0386e-05)
mat.add_element('Ar', 4.6160e-07)
mat.add_element('C', 1.6307e-08)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 4.7716e-04)
mat.add_nuclide('U235', 4.4267e-02)
mat.add_nuclide('U238', 2.7350e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Beryllium (outer)"
mat.set_density('sum')
mat.add_element('Be', 1.2295e-01)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mats.export_to_xml()
