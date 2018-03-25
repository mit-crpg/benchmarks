import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.1923e-02)
mat.add_nuclide('Pu240', 4.6622e-03)
mat.add_nuclide('Pu241', 7.3273e-04)
mat.add_element('Fe', 3.1294e-04)
mat.add_element('C', 1.2949e-03)
mat.add_element('H', 3.0212e-04)
mat.add_element('N', 3.2610e-05)
mat.add_element('O', 4.8343e-05)
mats.append(mat)

mats.export_to_xml()
