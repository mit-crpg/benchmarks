import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6850e-02)
mat.add_nuclide('Pu240', 6.7365e-04)
mat.add_element('Ga', 2.3193e-03)
mat.add_element('C', 3.0426e-04)
mat.add_element('Ni', 1.6700e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Layer 2"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6579e-02)
mat.add_nuclide('Pu240', 6.6875e-04)
mat.add_element('Ga', 2.3155e-03)
mat.add_element('C', 3.0205e-04)
mat.add_element('Ni', 1.9330e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Layer 3"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6512e-02)
mat.add_nuclide('Pu240', 6.6739e-04)
mat.add_element('Ga', 2.2978e-03)
mat.add_element('C', 2.2608e-04)
mat.add_element('Ni', 2.3056e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Layer 4"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6576e-02)
mat.add_nuclide('Pu240', 6.6878e-04)
mat.add_element('Ga', 2.3286e-03)
mat.add_element('C', 3.0206e-04)
mat.add_element('Ni', 1.8631e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Layer 5"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6471e-02)
mat.add_nuclide('Pu240', 6.6665e-04)
mat.add_element('Ga', 2.2823e-03)
mat.add_element('C', 3.0110e-04)
mat.add_element('Ni', 1.9715e-03)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Lead reflector"
mat.set_density('sum')
mat.add_element('Pb', 3.2744e-02)
mat.add_element('Fe', 1.8347e-05)
mats.append(mat)

mats.export_to_xml()
