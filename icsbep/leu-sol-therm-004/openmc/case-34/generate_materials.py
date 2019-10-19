import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2203e-07)
mat.add_nuclide('U235', 6.4780e-05)
mat.add_nuclide('U236', 6.4700e-08)
mat.add_nuclide('U238', 5.7701e-04)
mat.add_nuclide('H1', 5.8032e-02)
mat.add_nuclide('N14', 2.6337e-03)
mat.add_element('O', 3.7527e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Stainless steel"
mat.set_density('sum')
mat.add_element('C', 4.3736e-05)
mat.add_element('Si', 1.0627e-03)
mat.add_element('Mn', 1.1561e-03)
mat.add_element('P', 1.3170e-05)
mat.add_element('S', 1.9782e-06)
mat.add_element('Ni', 8.3403e-03)
mat.add_element('Cr', 1.6775e-02)
mat.add_element('Fe', 5.9421e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 25 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6658e-02)
mat.add_element('O', 3.3329e-02)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Air"
mat.set_density('sum')
mat.add_nuclide('N14', 3.9016e-05)
mat.add_element('O', 1.0409e-05)
mats.append(mat)

mats.export_to_xml()
