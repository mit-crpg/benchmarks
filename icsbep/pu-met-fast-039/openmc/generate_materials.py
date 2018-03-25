import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6581e-02)
mat.add_nuclide('Pu240', 6.6880e-04)
mat.add_element('Ga', 2.3152e-03)
mat.add_element('C', 3.0207e-04)
mat.add_element('Ni', 1.9212e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Layer 2"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6512e-02)
mat.add_nuclide('Pu240', 6.6739e-04)
mat.add_element('Ga', 2.2978e-03)
mat.add_element('C', 2.2608e-04)
mat.add_element('Ni', 2.3056e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Layer 3"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6576e-02)
mat.add_nuclide('Pu240', 6.6878e-04)
mat.add_element('Ga', 2.3286e-03)
mat.add_element('C', 3.0206e-04)
mat.add_element('Ni', 1.8631e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Layer 4"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6471e-02)
mat.add_nuclide('Pu240', 6.6665e-04)
mat.add_element('Ga', 2.2823e-03)
mat.add_element('C', 3.0110e-04)
mat.add_element('Ni', 1.9715e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Layer 5"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6707e-02)
mat.add_nuclide('Pu240', 6.7110e-04)
mat.add_element('Ga', 2.3236e-03)
mat.add_element('C', 3.0311e-04)
mat.add_element('Ni', 1.6483e-03)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Duralumin reflector, layer 1"
mat.set_density('sum')
mat.add_element('Al', 5.5645e-02)
mat.add_element('Fe', 1.0183e-03)
mat.add_element('Cu', 1.0484e-03)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Duralumin reflector, layer 2"
mat.set_density('sum')
mat.add_element('Al', 5.3497e-02)
mat.add_element('Fe', 9.7902e-04)
mat.add_element('Cu', 1.0079e-03)
mats.append(mat)

mat = openmc.Material(8)
mat.name = "Duralumin reflector, layer 3"
mat.set_density('sum')
mat.add_element('Al', 5.1557e-02)
mat.add_element('Fe', 9.4353e-04)
mat.add_element('Cu', 9.7136e-04)
mats.append(mat)

mats.export_to_xml()
