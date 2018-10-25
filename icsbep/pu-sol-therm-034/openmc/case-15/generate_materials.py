import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "fissile solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 4.0405e-07)
mat.add_nuclide('Pu239', 8.2920e-04)
mat.add_nuclide('Pu240', 7.6302e-05)
mat.add_nuclide('Pu241', 7.7173e-06)
mat.add_nuclide('Pu242', 4.4252e-07)
mat.add_element('Gd', 7.7549e-05)
mat.add_nuclide('H1', 4.8973e-02)
mat.add_element('N', 6.1586e-03)
mat.add_element('O', 4.1728e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "304L stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 6.3278e-02)
mat.add_element('Cr', 1.6532e-02)
mat.add_element('Ni', 6.5095e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 23 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6691e-02)
mat.add_element('O', 3.3346e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mats.export_to_xml()
