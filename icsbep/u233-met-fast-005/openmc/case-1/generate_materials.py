import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "U233 core"
mat.set_density('sum')
mat.add_nuclide('U233', 4.7253e-02)
mat.add_nuclide('U234', 5.2705e-04)
mat.add_nuclide('U238', 3.2975e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Beryllium reflector"
mat.set_density('sum')
mat.add_element('Be', 1.1984e-01)
mat.add_element('O', 1.3776e-03)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mats.export_to_xml()
