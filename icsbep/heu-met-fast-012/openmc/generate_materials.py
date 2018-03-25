import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U235', 4.0999e-02)
mat.add_nuclide('U238', 4.0989e-03)
mat.add_nuclide('U234', 5.2246e-04)
mat.add_nuclide('U236', 8.7970e-05)
mat.add_element('C', 3.8652e-04)
mat.add_element('Fe', 1.3544e-04)
mat.add_element('W', 1.2414e-05)
mat.add_element('Cu', 7.2049e-04)
mat.add_element('Ni', 3.3433e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Aluminum reflector"
mat.set_density('sum')
mat.add_element('Al', 5.8566e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Copper"
mat.set_density('sum')
mat.add_element('Cu', 8.2365e-02)
mats.append(mat)

mats.export_to_xml()
