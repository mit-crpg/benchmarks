import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Zircaloy-2"
mat.set_density('sum')
mat.add_element('Zr', 4.2537e-02)
mat.add_element('Sn', 4.9918e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Polyethylene (0.9183 g/cm3)"
mat.set_density('sum')
mat.add_nuclide('H1', 7.8854e-02)
mat.add_element('C', 3.9427e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water (0.9982 g/cm3)"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6735e-02)
mat.add_element('O', 3.3368e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Borated Steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9259e-02)
mat.add_element('Cr', 1.7428e-02)
mat.add_element('Mn', 8.6816e-04)
mat.add_element('Ni', 7.5171e-03)
mat.add_nuclide('B10', 3.7488e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "UO2-ZrO2 Seed Fuel (97.29 w/o U-233)"
mat.set_density('sum')
mat.add_nuclide('U233', 3.9891e-03)
mat.add_nuclide('U234', 6.3690e-05)
mat.add_nuclide('U238', 4.5759e-05)
mat.add_element('O', 5.3932e-02)
mat.add_element('Zr', 2.2867e-02)
mats.append(mat)

mats.export_to_xml()
