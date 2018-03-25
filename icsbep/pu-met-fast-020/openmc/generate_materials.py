import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium alloy"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.3930e-02)
mat.add_nuclide('Pu240', 3.5043e-03)
mat.add_nuclide('Pu241', 3.9189e-04)
mat.add_element('Ga', 2.2105e-03)
mat.add_element('C', 3.0246e-04)
mat.add_element('Fe', 3.2525e-04)
mat.add_element('W', 7.4100e-05)
mat.add_element('Ni', 1.4187e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Depleted Uranium"
mat.set_density('sum')
mat.add_nuclide('U235', 2.3787e-04)
mat.add_nuclide('U238', 4.6738e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Duralumin"
mat.set_density('sum')
mat.add_element('Al', 5.8077e-02)
mat.add_element('Mg', 1.0332e-03)
mat.add_element('Mn', 1.8284e-04)
mat.add_element('Cu', 1.1329e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Fe"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mats.export_to_xml()
