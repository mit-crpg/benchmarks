import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "fissile solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 1.2912e-07)
mat.add_nuclide('Pu239', 2.6498e-04)
mat.add_nuclide('Pu240', 2.4383e-05)
mat.add_nuclide('Pu241', 2.4661e-06)
mat.add_nuclide('Pu242', 1.4141e-07)
mat.add_nuclide('H1', 6.0973e-02)
mat.add_element('N', 2.3203e-03)
mat.add_element('O', 3.6890e-02)
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
