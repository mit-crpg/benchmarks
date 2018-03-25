import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6623e-02)
mat.add_nuclide('Pu240', 6.6951e-04)
mat.add_element('Ga', 2.1979e-03)
mat.add_element('Fe', 1.4247e-04)
mat.add_element('C', 2.9311e-04)
mat.add_element('Ni', 1.8624e-03)
mats.append(mat)

mats.export_to_xml()
