import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "fissile solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 2.0831e-07)
mat.add_nuclide('Pu239', 4.2266e-05)
mat.add_nuclide('Pu240', 4.3641e-05)
mat.add_nuclide('Pu241', 1.1029e-05)
mat.add_nuclide('Pu242', 4.7482e-06)
mat.add_nuclide('Am241', 1.0949e-06)
mat.add_element('Gd', 1.3831e-08)
mat.add_nuclide('H1', 6.3362e-02)
mat.add_element('N', 1.2902e-03)
mat.add_element('O', 3.5112e-02)
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
