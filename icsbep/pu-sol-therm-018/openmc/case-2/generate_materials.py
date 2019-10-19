import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 5.9547e-07)
mat.add_nuclide('Pu239', 1.2082e-04)
mat.add_nuclide('Pu240', 1.2475e-04)
mat.add_nuclide('Pu241', 3.1528e-05)
mat.add_nuclide('Pu242', 1.3573e-05)
mat.add_nuclide('Am241', 3.1298e-06)
mat.add_element('Gd', 3.9537e-08)
mat.add_nuclide('H1', 5.7230e-02)
mat.add_element('N', 3.6678e-03)
mat.add_element('O', 3.8372e-02)
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
