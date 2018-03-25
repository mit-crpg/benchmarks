import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Enriched U metal (37.5 w/o)"
mat.set_density('sum')
mat.add_nuclide('U235', 1.7730e-02)
mat.add_nuclide('U238', 2.8957e-02)
mat.add_element('C', 1.8452e-04)
mat.add_element('O', 3.4631e-04)
mat.add_element('Fe', 5.9527e-05)
mat.add_element('Al', 4.1070e-05)
mat.add_element('H', 4.3978e-05)
mat.add_element('Si', 3.9456e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Natural U metal"
mat.set_density('sum')
mat.add_nuclide('U235', 3.3316e-04)
mat.add_nuclide('U238', 4.5948e-02)
mat.add_element('C', 4.9205e-04)
mat.add_element('Fe', 1.0583e-04)
mat.add_element('H', 4.3978e-05)
mat.add_element('Si', 2.1043e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Sheath"
mat.set_density('sum')
mat.add_element('C', 7.7829e-04)
mat.add_element('Fe', 5.6624e-02)
mat.add_element('Cr', 1.6107e-02)
mat.add_element('Cu', 7.3853e-05)
mat.add_element('Mo', 1.4635e-04)
mat.add_element('Mn', 1.1918e-03)
mat.add_element('Ni', 9.0041e-03)
mat.add_element('Al', 3.4646e-04)
mat.add_element('Ti', 2.9326e-04)
mat.add_element('H', 2.2714e-05)
mat.add_element('Si', 9.9988e-04)
mat.add_element('V', 9.2127e-05)
mats.append(mat)

mats.export_to_xml()
