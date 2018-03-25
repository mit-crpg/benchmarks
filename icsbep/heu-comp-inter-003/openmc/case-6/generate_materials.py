import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Aluminum"
mat.set_density('sum')
mat.add_nuclide('Al27', 6.0239e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Depleted Uranium"
mat.set_density('sum')
mat.add_nuclide('U235', 9.7360e-05)
mat.add_nuclide('U238', 4.7969e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "SAE 1020 Steel"
mat.set_density('sum')
mat.add_element('Fe', 6.9267e-02)
mat.add_element('C', 5.4977e-04)
mat.add_element('Mn', 1.6969e-04)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Fe"
mat.set_density('sum')
mat.add_element('Fe', 8.5834e-02)
mats.append(mat)

mat = openmc.Material(11)
mat.name = "HEU, Can I"
mat.set_density('sum')
mat.add_nuclide('U234', 2.5279e-04)
mat.add_nuclide('U235', 2.3450e-02)
mat.add_nuclide('U236', 1.1027e-04)
mat.add_nuclide('U238', 1.3421e-03)
mat.add_element('H', 7.3871e-02)
mat.add_element('O', 8.5553e-04)
mat.add_element('C', 1.4562e-04)
mat.add_element('N', 1.3593e-03)
mat.add_element('Fe', 3.6677e-05)
mat.add_element('Au', 3.3980e-04)
mats.append(mat)

mat = openmc.Material(12)
mat.name = "HEU, Can II"
mat.set_density('sum')
mat.add_nuclide('U234', 2.5484e-04)
mat.add_nuclide('U235', 2.3409e-02)
mat.add_nuclide('U236', 1.0757e-04)
mat.add_nuclide('U238', 1.3371e-03)
mat.add_element('H', 7.5396e-02)
mat.add_element('O', 5.6703e-04)
mat.add_element('C', 1.9893e-04)
mat.add_element('N', 1.9699e-04)
mat.add_element('Fe', 3.8266e-05)
mat.add_element('Au', 3.3787e-04)
mats.append(mat)

mat = openmc.Material(13)
mat.name = "HEU, Can III"
mat.set_density('sum')
mat.add_nuclide('U234', 2.5651e-04)
mat.add_nuclide('U235', 2.3550e-02)
mat.add_nuclide('U236', 1.0829e-04)
mat.add_nuclide('U238', 1.3584e-03)
mat.add_element('H', 6.9913e-02)
mat.add_element('O', 4.8424e-04)
mat.add_element('C', 1.5288e-04)
mat.add_element('N', 2.0644e-04)
mat.add_element('Fe', 1.0366e-04)
mat.add_element('Au', 3.4242e-04)
mats.append(mat)

mat = openmc.Material(14)
mat.name = "HEU, Can IV"
mat.set_density('sum')
mat.add_nuclide('U234', 2.4873e-04)
mat.add_nuclide('U235', 2.2939e-02)
mat.add_nuclide('U236', 1.0390e-04)
mat.add_nuclide('U238', 1.3117e-03)
mat.add_element('H', 7.2725e-02)
mat.add_element('O', 6.3713e-04)
mat.add_element('C', 1.5539e-04)
mat.add_element('N', 2.4400e-04)
mat.add_element('Fe', 2.0435e-05)
mat.add_element('Au', 3.4196e-04)
mats.append(mat)

mats.export_to_xml()
