import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution (19.7 g/L)"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.68825e-05)
mat.add_nuclide('Pu240', 9.34548e-06)
mat.add_nuclide('Pu241', 2.77030e-06)
mat.add_nuclide('Pu242', 5.59608e-07)
mat.add_nuclide('Am241', 3.00210e-07)
mat.add_element('N', 1.41344e-03)
mat.add_element('O', 3.53933e-02)
mat.add_nuclide('H1', 6.34983e-02)
mat.add_element('Fe', 4.96028e-06)
mat.add_element('Cr', 1.59511e-06)
mat.add_element('Ni', 1.13054e-06)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Air"
mat.set_density('sum')
mat.add_nuclide('O16', 1.0784e-05)
mat.add_nuclide('N14', 4.3090e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 6.1344e-02)
mat.add_element('Cr', 1.6472e-02)
mat.add_element('Ni', 8.1050e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Lucoflex"
mat.set_density('sum')
mat.add_element('C', 2.7365e-02)
mat.add_nuclide('H1', 4.1047e-02)
mat.add_element('Cl', 1.3682e-02)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Water"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6688e-02)
mat.add_element('O', 3.3344e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
