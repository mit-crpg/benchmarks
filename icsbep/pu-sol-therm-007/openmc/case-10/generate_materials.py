import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 1.4192e-08)
mat.add_nuclide('Pu239', 2.2379e-04)
mat.add_nuclide('Pu240', 1.0949e-05)
mat.add_nuclide('Pu241', 7.1243e-07)
mat.add_nuclide('Pu242', 2.0935e-08)
mat.add_nuclide('N14', 1.1703e-03)
mat.add_nuclide('H1', 6.3783e-02)
mat.add_nuclide('O16', 3.5288e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "304L stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9355e-02)
mat.add_element('Cr', 1.7428e-02)
mat.add_element('Ni', 7.7203e-03)
mat.add_element('Mn', 1.7363e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 25 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6655e-02)
mat.add_nuclide('O16', 3.3327e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
