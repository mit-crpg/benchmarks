import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2111e-04)
mat.add_nuclide('U235', 4.2064e-02)
mat.add_nuclide('U238', 4.3626e-03)
mat.add_element('C', 1.1074e-03)
mat.add_element('Fe', 1.9320e-04)
mat.add_element('W', 5.3798e-05)
mats.append(mat)

mats.export_to_xml()
