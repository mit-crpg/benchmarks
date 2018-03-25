import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.7047e-02)
mat.add_nuclide('Pu240', 1.7512e-03)
mat.add_nuclide('Pu241', 1.1674e-04)
mat.add_element('Ga', 1.3752e-03)
mats.append(mat)

mats.export_to_xml()
