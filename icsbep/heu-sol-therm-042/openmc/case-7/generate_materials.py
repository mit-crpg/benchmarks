import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 3.8070e-07)
mat.add_nuclide('U235', 3.3180e-05)
mat.add_nuclide('U236', 2.3146e-07)
mat.add_nuclide('U238', 1.9456e-06)
mat.add_nuclide('N14', 1.3695e-04)
mat.add_nuclide('H1', 6.6369e-02)
mat.add_element('O', 3.3634e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "SS-304 Tank"
mat.set_density('sum')
mat.add_element('Fe', 5.8200e-02)
mat.add_element('C', 3.1687e-04)
mat.add_element('Cr', 1.5554e-02)
mat.add_element('Ni', 9.7273e-03)
mat.add_element('Mo', 1.2397e-03)
mat.add_element('N', 3.3966e-04)
mats.append(mat)

mats.export_to_xml()
