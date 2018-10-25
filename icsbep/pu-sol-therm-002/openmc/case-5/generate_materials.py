import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu239', 1.5456e-04)
mat.add_nuclide('Pu240', 4.9568e-06)
mat.add_nuclide('N14', 2.6223e-03)
mat.add_nuclide('H1', 6.0707e-02)
mat.add_nuclide('O16', 3.7228e-02)
mat.add_element('Fe', 2.1243e-06)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "347 stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 6.0386e-02)
mat.add_element('Cr', 1.6678e-02)
mat.add_element('Ni', 9.8504e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 27 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6622e-02)
mat.add_nuclide('O16', 3.3311e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
