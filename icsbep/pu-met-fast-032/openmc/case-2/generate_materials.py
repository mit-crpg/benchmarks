import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.2126e-02)
mat.add_nuclide('Pu240', 4.5761e-03)
mat.add_nuclide('Pu241', 6.7271e-04)
mat.add_element('Fe', 2.8619e-04)
mat.add_element('C', 1.2600e-03)
mat.add_element('H', 3.2400e-04)
mat.add_element('N', 3.4972e-05)
mat.add_element('O', 5.1843e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Steel reflector"
mat.set_density('sum')
mat.add_element('Fe', 7.9924e-02)
mat.add_element('C', 1.1341e-03)
mat.add_element('Si', 1.6167e-04)
mat.add_element('Cr', 2.6198e-04)
mat.add_element('Mn', 3.3061e-04)
mat.add_element('Ni', 2.3210e-04)
mat.add_element('Cu', 2.1437e-04)
mats.append(mat)

mats.export_to_xml()
