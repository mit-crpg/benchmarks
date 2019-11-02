import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.1969e-04)
mat.add_nuclide('U235', 4.1018e-02)
mat.add_nuclide('U236', 8.9938e-05)
mat.add_nuclide('U238', 4.0942e-03)
mat.add_element('C', 4.0450e-04)
mat.add_element('Fe', 1.4271e-04)
mat.add_element('W', 1.2395e-05)
mat.add_element('Cu', 7.5891e-04)
mat.add_element('Ni', 3.5216e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Polyethylene"
mat.set_density('sum')
mat.add_element('C', 3.9047e-02)
mat.add_nuclide('H1', 7.8094e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Fe"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mats.export_to_xml()
