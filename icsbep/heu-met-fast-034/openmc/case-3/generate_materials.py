import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U235', 4.5694e-02)
mat.add_nuclide('U238', 1.3350e-03)
mat.add_nuclide('U234', 5.6419e-04)
mat.add_element('C', 7.4560e-05)
mat.add_element('Fe', 1.8040e-05)
mat.add_element('W', 9.1332e-07)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Polyethylene"
mat.set_density('sum')
mat.add_element('C', 3.9290e-02)
mat.add_nuclide('H1', 7.8579e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Titanium"
mat.set_density('sum')
mat.add_element('Ti', 5.6632e-02)
mat.add_element('Al', 1.0151e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Aluminium"
mat.set_density('sum')
mat.add_element('Al', 5.9154e-02)
mat.add_element('Mn', 3.8519e-04)
mat.add_element('Si', 1.7387e-04)
mat.add_element('Fe', 1.0202e-04)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Steel"
mat.set_density('sum')
mat.add_element('Fe', 8.2807e-02)
mat.add_element('C', 4.0815e-04)
mat.add_element('Si', 4.4883e-04)
mat.add_element('Mn', 4.2492e-04)
mat.add_element('Cr', 6.7345e-05)
mats.append(mat)

mats.export_to_xml()
