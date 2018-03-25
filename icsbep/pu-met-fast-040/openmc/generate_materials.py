import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6849e-02)
mat.add_nuclide('Pu240', 6.7362e-04)
mat.add_element('Ga', 2.3193e-03)
mat.add_element('C', 3.0425e-04)
mat.add_element('Ni', 1.4908e-03)
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
mat.name = "Copper reflector"
mat.set_density('sum')
mat.add_element('Cu', 8.4168e-02)
mat.add_element('Fe', 5.0504e-06)
mats.append(mat)

mats.export_to_xml()
