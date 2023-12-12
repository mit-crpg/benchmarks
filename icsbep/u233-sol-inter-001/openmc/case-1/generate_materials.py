import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "IEU Flouride Solution"
mat.set_density('g/cm3', 1.9712)
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
mat.set_density('g/cm3', 8.0)
mat.add_nuclide('Fe54', 0.0035799456)
mat.add_nuclide('Fe56', 0.05619748992)
mat.add_nuclide('Fe57', 0.00129784512)
mat.add_nuclide('Fe58', 0.00017271936)
mat.add_nuclide('Cr50', 0.0007246591)
mat.add_nuclide('Cr52', 0.01397432942)
mat.add_nuclide('Cr53', 0.00158457678)
mat.add_nuclide('Cr54', 0.0003944347)
mat.add_nuclide('Ni58', 0.0061448933016)
mat.add_nuclide('Ni60', 0.0023670018984)
mat.add_nuclide('Ni61', 0.0001028919336)
mat.add_nuclide('Ni62', 0.000328064508)
mat.add_nuclide('Ni64', 8.35483584e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Beryllium reflector"
mat.set_density('g/cm3', 1.82)
mat.add_nuclide('Be', 1.2161e-01)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mats.export_to_xml()
