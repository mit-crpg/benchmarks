import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.7592e-02)
mat.add_nuclide('Pu240', 1.9349e-03)
mat.add_nuclide('Pu241', 1.1797e-04)
mat.add_element('Ga', 1.3733e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.set_density('sum')
mat.add_element('Al', 5.8787e-02)
mat.add_element('Cu', 1.1759e-03)
mat.add_element('Si', 2.4187e-04)
mat.add_element('Mn', 2.4729e-04)
mat.add_element('Mg', 3.4936e-04)
mats.append(mat)

mats.export_to_xml()
