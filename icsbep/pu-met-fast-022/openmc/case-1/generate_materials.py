import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6826e-02)
mat.add_nuclide('Pu240', 6.7320e-04)
mat.add_element('Ga', 2.2000e-03)
mat.add_element('Fe', 1.4714e-04)
mat.add_element('C', 3.0406e-04)
mat.add_element('Ni', 1.5722e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Layer 2"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6579e-02)
mat.add_nuclide('Pu240', 6.6875e-04)
mat.add_element('Ga', 2.2114e-03)
mat.add_element('Fe', 1.2992e-04)
mat.add_element('C', 3.0205e-04)
mat.add_element('Ni', 1.9330e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Layer 3"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6512e-02)
mat.add_nuclide('Pu240', 6.6739e-04)
mat.add_element('Ga', 2.1940e-03)
mat.add_element('Fe', 1.2966e-04)
mat.add_element('C', 2.2608e-04)
mat.add_element('Ni', 2.3056e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Layer 4"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6576e-02)
mat.add_nuclide('Pu240', 6.6878e-04)
mat.add_element('Ga', 2.2115e-03)
mat.add_element('Fe', 1.4617e-04)
mat.add_element('C', 3.0206e-04)
mat.add_element('Ni', 1.8631e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Layer 5"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6471e-02)
mat.add_nuclide('Pu240', 6.6665e-04)
mat.add_element('Ga', 2.1656e-03)
mat.add_element('Fe', 1.4571e-04)
mat.add_element('C', 3.0110e-04)
mat.add_element('Ni', 1.9715e-03)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Layer 6"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6728e-02)
mat.add_nuclide('Pu240', 6.7147e-04)
mat.add_element('Ga', 2.2074e-03)
mat.add_element('Fe', 1.4676e-04)
mat.add_element('C', 3.0328e-04)
mat.add_element('Ni', 1.6492e-03)
mats.append(mat)

mats.export_to_xml()
