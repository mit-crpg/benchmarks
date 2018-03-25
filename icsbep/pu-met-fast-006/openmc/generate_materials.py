import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6697e-02)
mat.add_nuclide('Pu240', 1.8700e-03)
mat.add_nuclide('Pu241', 1.1639e-04)
mat.add_element('Ga', 1.4755e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.set_density('sum')
mat.add_nuclide('U234', 2.6438e-06)
mat.add_nuclide('U235', 3.4610e-04)
mat.add_nuclide('U238', 4.7721e-02)
mats.append(mat)

mats.export_to_xml()
