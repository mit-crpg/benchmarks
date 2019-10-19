import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6603e-02)
mat.add_nuclide('Pu240', 6.6913e-04)
mat.add_element('Ga', 2.1956e-03)
mat.add_element('Fe', 1.4086e-04)
mat.add_element('C', 2.8927e-04)
mat.add_element('Ni', 1.9484e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "c_Graphite"
mat.set_density('sum')
mat.add_element('C', 9.1842e-02)
mat.add_s_alpha_beta('c_Graphite')
mats.append(mat)

mats.export_to_xml()
