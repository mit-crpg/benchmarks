import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.1607e-02)
mat.add_nuclide('Pu240', 4.8551e-03)
mat.add_nuclide('Pu241', 9.0948e-04)
mat.add_element('Fe', 3.0510e-04)
mat.add_element('C', 1.9920e-03)
mat.add_element('H', 8.3342e-04)
mat.add_element('N', 8.9958e-05)
mat.add_element('O', 1.3336e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Layer 2"
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.2276e-02)
mat.add_nuclide('Pu240', 4.6060e-03)
mat.add_nuclide('Pu241', 6.7147e-04)
mat.add_element('Fe', 2.6534e-04)
mat.add_element('C', 1.1053e-03)
mat.add_element('H', 2.0011e-04)
mat.add_element('N', 2.1600e-05)
mat.add_element('O', 3.2020e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Layer 3"
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.1681e-02)
mat.add_nuclide('Pu240', 4.7176e-03)
mat.add_nuclide('Pu241', 7.4079e-04)
mat.add_element('Fe', 3.0356e-04)
mat.add_element('C', 1.1922e-03)
mat.add_element('H', 2.7505e-04)
mat.add_element('N', 2.9688e-05)
mat.add_element('O', 4.4011e-05)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Layer 4"
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.2431e-02)
mat.add_nuclide('Pu240', 4.3997e-03)
mat.add_nuclide('Pu241', 5.9425e-04)
mat.add_element('Fe', 2.8500e-04)
mat.add_element('C', 1.3956e-03)
mat.add_element('H', 4.3308e-04)
mat.add_element('N', 4.6746e-05)
mat.add_element('O', 6.9297e-05)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Steel reflector"
mat.set_density('sum')
mat.add_element('Fe', 7.9924e-02)
mat.add_element('C', 1.1341e-03)
mat.add_element('Si', 1.6167e-04)
mat.add_element('Cr', 2.6198e-04)
mat.add_element('Mn', 3.3061e-04)
mat.add_element('Ni', 2.3210e-04)
mat.add_element('Cu', 2.1437e-04)
mats.append(mat)

mats.export_to_xml()
