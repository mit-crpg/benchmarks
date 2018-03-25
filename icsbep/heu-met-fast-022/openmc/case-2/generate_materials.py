import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2104e-04)
mat.add_nuclide('U235', 4.2055e-02)
mat.add_nuclide('U238', 4.3629e-03)
mat.add_element('C', 1.0482e-03)
mat.add_element('Fe', 1.8514e-04)
mat.add_element('W', 5.1713e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Duralumin reflector"
mat.set_density('sum')
mat.add_element('Al', 5.3934e-02)
mat.add_element('Fe', 9.8702e-04)
mat.add_element('Cu', 1.0161e-03)
mats.append(mat)

mats.export_to_xml()
