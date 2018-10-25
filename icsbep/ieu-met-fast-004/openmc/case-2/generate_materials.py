import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "36 wt% U-235"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5652e-04)
mat.add_nuclide('U235', 1.7384e-02)
mat.add_nuclide('U238', 2.9662e-02)
mat.add_element('C', 6.5752e-04)
mat.add_element('Fe', 1.2098e-04)
mat.add_element('W', 1.0121e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "c_Graphite"
mat.set_density('sum')
mat.add_element('C', 7.7716e-02)
mat.add_s_alpha_beta('c_Graphite')
mats.append(mat)

mats.export_to_xml()
