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
mat.add_nuclide('U235', 3.4902e-04)
mat.add_nuclide('U238', 4.7518e-02)
mats.append(mat)

mats.export_to_xml()
