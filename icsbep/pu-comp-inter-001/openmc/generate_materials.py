import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('Pu239', 2.735e-04)
mat.add_nuclide('Pu240', 1.549e-05)
mat.add_nuclide('Pu241', 1.072e-06)
mat.add_nuclide('Pu242', 5.800e-08)
mat.add_nuclide('H1', 1.077e-04)
mat.add_nuclide('B10', 1.0151e-04)
mat.add_nuclide('B11', 4.0859e-04)
mat.add_element('C', 7.090e-02)
mat.add_element('O', 2.707e-03)
mat.add_element('Ca', 8.280e-04)
mat.add_s_alpha_beta('c_Graphite')
mats.append(mat)

mats.export_to_xml()
