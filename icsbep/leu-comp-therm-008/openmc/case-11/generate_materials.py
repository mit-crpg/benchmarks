import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Water with 1384 PPM Boron"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6737e-02)
mat.add_nuclide('O16', 3.3369e-02)
mat.add_nuclide('B10', 1.5359e-05)
mat.add_nuclide('B11', 6.1824e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Fuel (2.459 w/o with B-10 for impurities)"
mat.set_density('sum')
mat.add_nuclide('U234', 4.5689e-06)
mat.add_nuclide('U235', 5.6868e-04)
mat.add_nuclide('U238', 2.2268e-02)
mat.add_nuclide('O16', 4.5683e-02)
mat.add_nuclide('B10', 2.6055e-07)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Aluminum 6061 Cladding for Fuel"
mat.set_density('sum')
mat.add_element('Mg', 6.2072e-04)
mat.add_element('Al', 5.3985e-02)
mat.add_element('Si', 3.2230e-04)
mat.add_element('Ti', 4.7263e-05)
mat.add_element('Cr', 5.8029e-05)
mat.add_element('Mn', 4.1191e-05)
mat.add_element('Fe', 1.8910e-04)
mat.add_element('Cu', 5.9353e-05)
mat.add_element('Zn', 5.7679e-05)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Al2O3"
mat.set_density('sum')
mat.add_nuclide('O16', 2.3036e-02)
mat.add_nuclide('Al27', 1.5357e-02)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Cladding for Al2O3 Perturbing Rods"
mat.set_density('sum')
mat.add_element('Mg', 6.6898e-04)
mat.add_element('Al', 5.8183e-02)
mat.add_element('Si', 3.4736e-04)
mat.add_element('Ti', 5.0939e-05)
mat.add_element('Cr', 6.2542e-05)
mat.add_element('Mn', 4.4395e-05)
mat.add_element('Fe', 2.0380e-04)
mat.add_element('Cu', 6.3968e-05)
mat.add_element('Zn', 6.2164e-05)
mats.append(mat)

mats.export_to_xml()
