import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6182e-02)
mat.add_nuclide('Pu240', 6.6143e-04)
mat.add_element('Ga', 2.1486e-03)
mat.add_element('Fe', 1.6063e-04)
mat.add_element('C', 2.9874e-04)
mat.add_element('Ni', 4.2529e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Layer 2"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6826e-02)
mat.add_nuclide('Pu240', 6.7320e-04)
mat.add_element('Ga', 2.2000e-03)
mat.add_element('Fe', 1.4714e-04)
mat.add_element('C', 3.0406e-04)
mat.add_element('Ni', 1.5722e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Layer 3"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6711e-02)
mat.add_nuclide('Pu240', 6.7117e-04)
mat.add_element('Ga', 2.2194e-03)
mat.add_element('Fe', 1.3039e-04)
mat.add_element('C', 3.0315e-04)
mat.add_element('Ni', 1.9400e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Layer 4"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6632e-02)
mat.add_nuclide('Pu240', 6.6958e-04)
mat.add_element('Ga', 2.2012e-03)
mat.add_element('Fe', 1.3009e-04)
mat.add_element('C', 2.2682e-04)
mat.add_element('Ni', 2.3132e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Layer 5"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6725e-02)
mat.add_nuclide('Pu240', 6.7150e-04)
mat.add_element('Ga', 2.2205e-03)
mat.add_element('Fe', 1.4677e-04)
mat.add_element('C', 3.0329e-04)
mat.add_element('Ni', 1.8706e-03)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Layer 6"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6654e-02)
mat.add_nuclide('Pu240', 6.6998e-04)
mat.add_element('Ga', 2.1764e-03)
mat.add_element('Fe', 1.4643e-04)
mat.add_element('C', 3.0261e-04)
mat.add_element('Ni', 1.9814e-03)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Steel reflector"
mat.set_density('sum')
mat.add_element('Fe', 7.9557e-02)
mat.add_element('C', 1.1289e-03)
mat.add_element('Si', 1.6093e-04)
mat.add_element('Cr', 2.6078e-04)
mat.add_element('Mn', 3.2909e-04)
mat.add_element('Ni', 2.3104e-04)
mat.add_element('Cu', 2.1338e-04)
mats.append(mat)

mats.export_to_xml()
