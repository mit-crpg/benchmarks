import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium core"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6049e-02)
mat.add_nuclide('Pu240', 1.9562e-03)
mat.add_nuclide('Pu241', 1.1459e-04)
mat.add_element('Ga', 1.3338e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Thorium reflector"
mat.set_density('sum')
mat.add_nuclide('Th232', 3.0054e-02)
mats.append(mat)

mats.export_to_xml()
