import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.3928e-02)
mat.add_nuclide('Pu240', 3.5032e-03)
mat.add_nuclide('Pu241', 3.9158e-04)
mat.add_element('Ga', 2.2104e-03)
mat.add_element('C', 3.0244e-04)
mat.add_element('Fe', 3.2523e-04)
mat.add_element('W', 7.4094e-05)
mat.add_element('Ni', 1.4266e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U235', 4.1081e-02)
mat.add_nuclide('U238', 4.1002e-03)
mat.add_nuclide('U234', 5.2253e-04)
mat.add_nuclide('U236', 8.8981e-05)
mat.add_element('C', 3.8650e-04)
mat.add_element('Fe', 1.5027e-04)
mat.add_element('W', 1.2329e-05)
mat.add_element('Cu', 7.3626e-04)
mat.add_element('Ni', 3.4165e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Iron"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Copper"
mat.set_density('sum')
mat.add_element('Cu', 8.2365e-02)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Duralumin"
mat.set_density('sum')
mat.add_element('Al', 5.8077e-02)
mat.add_element('Mg', 1.0332e-03)
mat.add_element('Mn', 1.8284e-04)
mat.add_element('Cu', 1.1329e-03)
mats.append(mat)

mats.export_to_xml()
