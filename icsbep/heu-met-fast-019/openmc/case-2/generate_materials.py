import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2315e-04)
mat.add_nuclide('U235', 4.2256e-02)
mat.add_nuclide('U238', 4.3799e-03)
mat.add_element('C', 1.0894e-03)
mat.add_element('Fe', 1.9121e-04)
mat.add_element('W', 5.3019e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "c_Graphite"
mat.set_density('sum')
mat.add_element('C', 7.6716e-02)
mat.add_s_alpha_beta('c_Graphite')
mats.append(mat)

mats.export_to_xml()
