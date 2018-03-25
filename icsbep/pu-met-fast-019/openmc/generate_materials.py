import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.3930e-02)
mat.add_nuclide('Pu240', 3.5043e-03)
mat.add_nuclide('Pu241', 3.9189e-04)
mat.add_element('Ga', 2.2105e-03)
mat.add_element('C', 3.0246e-03)
mat.add_element('Fe', 3.2525e-04)
mat.add_element('W', 7.4100e-05)
mat.add_element('Ni', 1.4187e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Reflector"
mat.set_density('sum')
mat.add_element('Be', 1.2081e-01)
mat.add_element('O', 8.2064e-05)
mat.add_element('C', 1.0020e-04)
mat.add_element('Fe', 5.0939e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel Diaphragm and Steel Shaft"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Copper Cup"
mat.set_density('sum')
mat.add_element('Cu', 8.2365e-02)
mats.append(mat)

mats.export_to_xml()
