import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6180e-02)
mat.add_nuclide('Pu240', 6.6139e-04)
mat.add_element('Ga', 2.1485e-03)
mat.add_element('Fe', 1.6062e-04)
mat.add_element('C', 2.9873e-04)
mat.add_element('Ni', 4.2527e-03)
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
mat.add_nuclide('Pu239', 3.6579e-02)
mat.add_nuclide('Pu240', 6.6875e-04)
mat.add_element('Ga', 2.2114e-03)
mat.add_element('Fe', 1.2992e-04)
mat.add_element('C', 3.0205e-04)
mat.add_element('Ni', 1.9330e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Layer 4"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6512e-02)
mat.add_nuclide('Pu240', 6.6739e-04)
mat.add_element('Ga', 2.1940e-03)
mat.add_element('Fe', 1.2966e-04)
mat.add_element('C', 2.2608e-04)
mat.add_element('Ni', 2.3056e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Layer 5"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6576e-02)
mat.add_nuclide('Pu240', 6.6878e-04)
mat.add_element('Ga', 2.2115e-03)
mat.add_element('Fe', 1.4617e-04)
mat.add_element('C', 3.0206e-04)
mat.add_element('Ni', 1.8631e-03)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Layer 6"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6616e-02)
mat.add_nuclide('Pu240', 6.6930e-04)
mat.add_element('Ga', 2.1742e-03)
mat.add_element('Fe', 1.4628e-04)
mat.add_element('C', 3.0230e-04)
mat.add_element('Ni', 1.9794e-03)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Polyethylene"
mat.set_density('sum')
mat.add_nuclide('H1', 7.7628e-02)
mat.add_element('C', 3.8814e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mats.export_to_xml()
