import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Pure Pu"
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.6010e-02)
mat.add_nuclide('Pu240', 2.9236e-03)
mat.add_nuclide('Pu241', 2.2433e-04)
mat.add_nuclide('Pu242', 4.8566e-06)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Aluminum"
mat.set_density('sum')
mat.add_element('Al', 6.0263e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.3031e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Al Heat Sink: Top"
mat.set_density('sum')
mat.add_element('Al', 3.6742e-02)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Al Heat Sink: Bottom"
mat.set_density('sum')
mat.add_element('Al', 3.0139e-02)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Steel"
mat.set_density('sum')
mat.add_element('Fe', 8.4122e-02)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Steel (Table Support at 7% density)"
mat.set_density('sum')
mat.add_element('Fe', 5.8885e-03)
mats.append(mat)

mat = openmc.Material(8)
mat.name = "Stainless Steel: Shoe"
mat.set_density('sum')
mat.add_element('Al', 2.9260e-02)
mat.add_element('Fe', 7.7911e-03)
mats.append(mat)

mats.export_to_xml()
