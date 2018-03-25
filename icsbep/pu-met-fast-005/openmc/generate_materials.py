import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.7291e-02)
mat.add_nuclide('Pu240', 1.9277e-03)
mat.add_nuclide('Pu241', 1.2196e-04)
mat.add_element('Ga', 1.3628e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.set_density('sum')
mat.add_element('W', 5.1468e-02)
mat.add_element('Ni', 9.7124e-03)
mat.add_element('Cu', 4.0774e-03)
mat.add_element('Zr', 7.9528e-04)
mats.append(mat)

mats.export_to_xml()
