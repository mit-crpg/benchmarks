import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution (16.7 g/L)"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.12659e-05)
mat.add_nuclide('Pu240', 7.92231e-06)
mat.add_nuclide('Pu241', 2.34842e-06)
mat.add_nuclide('Pu242', 4.74388e-07)
mat.add_nuclide('Am241', 2.54492e-07)
mat.add_element('N', 1.38532e-03)
mat.add_element('O', 3.53767e-02)
mat.add_nuclide('H1', 6.36398e-02)
mat.add_element('Fe', 4.09762e-06)
mat.add_element('Cr', 1.31770e-06)
mat.add_element('Ni', 9.33923e-07)
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

mat = openmc.Material(6)
mat.name = "Steel (pool wall)"
mat.set_density('sum')
mat.add_element('Fe', 8.5068e-02)
mat.add_element('C', 5.5545e-04)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Concrete"
mat.set_density('sum')
mat.add_nuclide('H1', 1.035e-02)
mat.add_nuclide('B10', 1.602e-06)
mat.add_element('O', 4.347e-02)
mat.add_element('Al', 1.563e-03)
mat.add_element('Si', 1.417e-02)
mat.add_element('Ca', 6.424e-03)
mat.add_element('Fe', 7.621e-04)
mats.append(mat)

mats.export_to_xml()
