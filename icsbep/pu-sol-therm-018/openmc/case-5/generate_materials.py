import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 3.8829e-07)
mat.add_nuclide('Pu239', 7.8783e-05)
mat.add_nuclide('Pu240', 8.1345e-05)
mat.add_nuclide('Pu241', 2.0559e-05)
mat.add_nuclide('Pu242', 8.8504e-06)
mat.add_nuclide('Am241', 2.0408e-06)
mat.add_element('Gd', 2.5781e-08)
mat.add_nuclide('H1', 6.0457e-02)
mat.add_element('N', 2.4160e-03)
mat.add_element('O', 3.6651e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "steel clad"
mat.set_density('sum')
mat.add_element('Fe', 6.3278e-02)
mat.add_element('Cr', 1.6532e-02)
mat.add_element('Ni', 6.5095e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "water"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6691e-02)
mat.add_element('O', 3.3346e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
