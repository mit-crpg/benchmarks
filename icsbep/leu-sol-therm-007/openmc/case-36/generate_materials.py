import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2265e-07)
mat.add_nuclide('U235', 6.4857e-05)
mat.add_nuclide('U236', 6.4776e-08)
mat.add_nuclide('U238', 5.7769e-04)
mat.add_nuclide('H1', 5.8115e-02)
mat.add_element('N', 2.6292e-03)
mat.add_element('O', 3.7560e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Stainless Steel"
mat.set_density('sum')
mat.add_element('C', 4.3736e-05)
mat.add_element('Si', 1.0627e-03)
mat.add_element('Mn', 1.1561e-03)
mat.add_element('P', 4.3170e-05)
mat.add_element('S', 2.9782e-06)
mat.add_element('Ni', 8.3403e-03)
mat.add_element('Cr', 1.6775e-02)
mat.add_element('Fe', 5.9421e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Air"
mat.set_density('sum')
mat.add_element('N', 3.9016e-05)
mat.add_element('O', 1.0409e-05)
mats.append(mat)

mats.export_to_xml()
