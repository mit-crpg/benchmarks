import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Tuballoy"
mat.set_density('sum')
mat.add_nuclide('U234', 2.6428e-06)
mat.add_nuclide('U235', 3.4597e-04)
mat.add_nuclide('U238', 4.7702e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Oralloy"
mat.set_density('sum')
mat.add_nuclide('U234', 4.9157e-04)
mat.add_nuclide('U235', 4.4825e-02)
mat.add_nuclide('U238', 2.6391e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "2024 Aluminum"
mat.set_density('sum')
mat.add_element('Mg', 1.0295e-03)
mat.add_element('Al', 5.7868e-02)
mat.add_element('Mn', 1.5182e-04)
mat.add_element('Cu', 1.1550e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Stainless Steel"
mat.set_density('sum')
mat.add_element('Cr', 1.6532e-02)
mat.add_element('Fe', 6.3278e-02)
mat.add_element('Ni', 6.5095e-03)
mats.append(mat)

mats.export_to_xml()
