import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu239', 1.0484e-04)
mat.add_nuclide('Pu240', 4.5432e-06)
mat.add_nuclide('N14', 2.7369e-03)
mat.add_nuclide('H1', 6.0233e-02)
mat.add_nuclide('O16', 3.7177e-02)
mat.add_element('Fe', 1.9302e-06)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "347 Stainless Steel"
mat.set_density('sum')
mat.add_element('Fe', 6.0386e-02)
mat.add_element('Cr', 1.6678e-02)
mat.add_element('Ni', 9.8504e-03)
mats.append(mat)

mats.export_to_xml()
