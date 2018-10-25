import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2428e-04)
mat.add_nuclide('U235', 4.2315e-02)
mat.add_nuclide('U238', 4.3901e-03)
mat.add_element('C', 1.0548e-03)
mat.add_element('Fe', 1.8627e-04)
mat.add_element('W', 5.2040e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Polyethylene"
mat.set_density('sum')
mat.add_nuclide('H1', 7.7711e-02)
mat.add_element('C', 3.8856e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mats.export_to_xml()
