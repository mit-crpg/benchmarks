import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 4.9210e-04)
mat.add_nuclide('U235', 4.5010e-02)
mat.add_nuclide('U238', 2.4096e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "c_Graphite"
mat.set_density('sum')
mat.add_element('C', 8.3731e-02)
mat.add_s_alpha_beta('c_Graphite')
mats.append(mat)

mats.export_to_xml()
