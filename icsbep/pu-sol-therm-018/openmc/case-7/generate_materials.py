import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 2.8921e-07)
mat.add_nuclide('Pu239', 5.8681e-05)
mat.add_nuclide('Pu240', 6.0590e-05)
mat.add_nuclide('Pu241', 1.5313e-05)
mat.add_nuclide('Pu242', 6.5922e-06)
mat.add_nuclide('Am241', 1.5201e-06)
mat.add_element('Gd', 1.9203e-08)
mat.add_nuclide('H1', 6.2033e-02)
mat.add_element('N', 1.8050e-03)
mat.add_element('O', 3.5814e-02)
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
