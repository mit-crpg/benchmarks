import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2275e-04)
mat.add_nuclide('U235', 4.1032e-02)
mat.add_nuclide('U236', 8.8021e-05)
mat.add_nuclide('U238', 4.1010e-03)
mat.add_element('C', 3.9536e-04)
mat.add_element('Fe', 1.3512e-04)
mat.add_element('W', 1.2426e-05)
mat.add_element('Cu', 7.1251e-04)
mat.add_element('Ni', 3.3062e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Duralumin"
mat.set_density('sum')
mat.add_element('Al', 5.8077e-02)
mat.add_element('Mg', 1.0332e-03)
mat.add_element('Mn', 1.8284e-04)
mat.add_element('Cu', 1.1329e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Pure Fe"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Depleted Uranium"
mat.set_density('sum')
mat.add_nuclide('U235', 2.3832e-04)
mat.add_nuclide('U238', 4.6826e-02)
mats.append(mat)

mats.export_to_xml()
