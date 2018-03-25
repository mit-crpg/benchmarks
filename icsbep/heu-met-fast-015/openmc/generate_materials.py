import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Bottom HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.6597e-04)
mat.add_nuclide('U235', 4.5774e-02)
mat.add_nuclide('U238', 1.3381e-03)
mat.add_element('C', 1.0270e-04)
mat.add_element('Fe', 5.0201e-05)
mat.add_element('W', 1.2199e-06)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Top HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.6404e-04)
mat.add_nuclide('U235', 4.5708e-02)
mat.add_nuclide('U238', 1.3404e-03)
mat.add_element('C', 1.0256e-04)
mat.add_element('Fe', 5.0131e-05)
mat.add_element('W', 1.2183e-06)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel Diaphragm and Steel Plate"
mat.set_density('sum')
mat.add_element('Fe', 8.1133e-02)
mats.append(mat)

mats.export_to_xml()
