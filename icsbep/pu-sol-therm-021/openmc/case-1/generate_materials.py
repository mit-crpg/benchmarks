import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 5.9197e-09)
mat.add_nuclide('Pu239', 9.3366e-05)
mat.add_nuclide('Pu240', 4.5680e-06)
mat.add_nuclide('Pu241', 2.7573e-07)
mat.add_nuclide('Pu242', 8.7324e-09)
mat.add_nuclide('N14', 6.3382e-04)
mat.add_nuclide('H1', 6.5515e-02)
mat.add_nuclide('O16', 3.4538e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "304L Stainless Steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9355e-02)
mat.add_element('Cr', 1.7428e-02)
mat.add_element('Ni', 7.7203e-03)
mat.add_element('Mn', 1.7363e-03)
mats.append(mat)

mats.export_to_xml()
