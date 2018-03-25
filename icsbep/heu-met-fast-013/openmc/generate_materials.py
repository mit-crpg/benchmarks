import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2209e-04)
mat.add_nuclide('U235', 4.1011e-02)
mat.add_nuclide('U236', 8.8453e-05)
mat.add_nuclide('U238', 4.0989e-03)
mat.add_element('C', 3.9946e-04)
mat.add_element('Fe', 1.3536e-04)
mat.add_element('W', 1.2340e-05)
mat.add_element('Cu', 7.2932e-04)
mat.add_element('Ni', 3.3843e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Steel"
mat.set_density('sum')
mat.add_element('Fe', 8.2555e-02)
mat.add_element('C', 7.7554e-04)
mat.add_element('Si', 3.4825e-04)
mat.add_element('Cr', 6.7181e-05)
mat.add_element('Mn', 4.4508e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Pure Fe"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Copper"
mat.set_density('sum')
mat.add_element('Cu', 8.2365e-02)
mats.append(mat)

mats.export_to_xml()
