import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranium Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 5.3850e-07)
mat.add_nuclide('U235', 4.8042e-05)
mat.add_nuclide('U236', 1.3862e-07)
mat.add_nuclide('U238', 2.8050e-06)
mat.add_nuclide('N14', 1.8685e-04)
mat.add_nuclide('O16', 3.3629e-02)
mat.add_nuclide('O17', 1.2784e-05)
mat.add_nuclide('H1', 6.6041e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Type 1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9699e-02)
mat.add_element('Si', 5.5202e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mats.export_to_xml()
