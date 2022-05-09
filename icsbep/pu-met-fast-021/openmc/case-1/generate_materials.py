import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium"
mat.set_density('sum')
mat.add_nuclide('Pu239', 4.4422e-02)
mat.add_nuclide('Pu240', 2.1326e-03)
mat.add_nuclide('Pu241', 9.2538e-05)
mat.add_element('C', 1.9515e-04)
mat.add_element('Fe', 8.1943e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Berylium Reflector"
mat.set_density('sum')
mat.add_element('Be', 1.2099e-01)
mat.add_element('O', 1.0449e-03)
mat.add_s_alpha_beta('c_Be')
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel Cover"
mat.set_density('sum')
mat.add_element('Fe', 5.1280e-02)
mat.add_element('C', 3.4757e-04)
mat.add_element('Si', 8.9185e-04)
mat.add_element('Ti', 6.1034e-04)
mat.add_element('Cr', 1.4452e-02)
mat.add_element('Mn', 1.5198e-03)
mat.add_element('Ni', 7.1131e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Duralumin base and top (2.78 g/cm3)"
mat.set_density('sum')
mat.add_element('Al', 5.8077e-02)
mat.add_element('Mg', 1.0332e-03)
mat.add_element('Mn', 1.8284e-04)
mat.add_element('Cu', 1.1329e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Duralumin top cylindrical shell (0.417 g/cm3)"
mat.set_density('sum')
mat.add_element('Al', 8.7115e-03)
mat.add_element('Mg', 1.5498e-04)
mat.add_element('Mn', 2.7426e-05)
mat.add_element('Cu', 1.6993e-04)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Duralumin bottom cylindrical shell (1.8155 g/cm3)"
mat.set_density('sum')
mat.add_element('Al', 3.7928e-02)
mat.add_element('Mg', 6.7475e-04)
mat.add_element('Mn', 1.1941e-04)
mat.add_element('Cu', 7.3982e-04)
mats.append(mat)

mats.export_to_xml()
