import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "IEU Flouride Solution"
mat.set_density('sum')
mat.add_nuclide('U232', 4.5608e-08)
mat.add_nuclide('U233', 2.2379e-03)
mat.add_nuclide('U234', 2.4316e-05)
mat.add_nuclide('U235', 8.9598e-07)
mat.add_nuclide('U238', 7.1284e-06)
mat.add_nuclide('H1', 5.5183e-02)
mat.add_nuclide('O16', 3.2043e-02)
mat.add_nuclide('F19', 4.7182e-03)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "347 Stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 6.1248e-02)
mat.add_element('Cr', 1.6678e-02)
mat.add_element('Ni', 9.0264e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Beryllium reflector"
mat.set_density('sum')
mat.add_element('Be', 1.2161e-01)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mats.export_to_xml()
