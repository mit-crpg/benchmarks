import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6603e-02)
mat.add_nuclide('Pu240', 6.6917e-04)
mat.add_element('Ga', 2.2043e-03)
mat.add_element('Fe', 1.3906e-04)
mat.add_element('C', 2.8435e-04)
mat.add_element('Ni', 1.9642e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Steel reflector 1"
mat.set_density('sum')
mat.add_element('Fe', 7.9416e-02)
mat.add_element('C', 1.1269e-03)
mat.add_element('Si', 1.6065e-04)
mat.add_element('Cr', 2.6032e-04)
mat.add_element('Mn', 3.2850e-04)
mat.add_element('Ni', 2.3063e-04)
mat.add_element('Cu', 2.1300e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel reflector 2"
mat.set_density('sum')
mat.add_element('Fe', 7.8919e-02)
mat.add_element('C', 1.1199e-03)
mat.add_element('Si', 1.5964e-04)
mat.add_element('Cr', 2.5869e-04)
mat.add_element('Mn', 3.2645e-04)
mat.add_element('Ni', 2.2918e-04)
mat.add_element('Cu', 2.1167e-04)
mats.append(mat)

mats.export_to_xml()
