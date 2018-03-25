import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 2.9934e-02)
mat.add_nuclide('Pu240', 7.8754e-03)
mat.add_nuclide('Pu241', 1.2146e-03)
mat.add_nuclide('Pu242', 1.5672e-04)
mat.add_element('Ga', 1.3722e-03)
mats.append(mat)

mats.export_to_xml()
