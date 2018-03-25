import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6620e-02)
mat.add_nuclide('Pu240', 6.6944e-04)
mat.add_element('Ga', 2.1962e-03)
mat.add_element('Fe', 1.4126e-04)
mat.add_element('C', 2.8972e-04)
mat.add_element('Ni', 1.9748e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Polyethylene"
mat.set_density('sum')
mat.add_nuclide('H1', 7.7628e-02)
mat.add_element('C', 3.8814e-02)
mats.append(mat)

mats.export_to_xml()
