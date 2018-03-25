import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "36 wt% U-235"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5518e-04)
mat.add_nuclide('U235', 1.7161e-02)
mat.add_nuclide('U238', 2.9310e-02)
mat.add_element('W', 1.0721e-05)
mat.add_element('Fe', 1.2345e-04)
mat.add_element('C', 6.4888e-04)
mat.add_element('Cu', 2.6755e-04)
mat.add_element('Ni', 2.8969e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Duralumin reflector #1"
mat.set_density('sum')
mat.add_element('Al', 5.2342e-02)
mat.add_element('Fe', 9.5788e-04)
mat.add_element('Cu', 9.8614e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Duralumin reflector #2"
mat.set_density('sum')
mat.add_element('Al', 5.2067e-02)
mat.add_element('Fe', 9.5286e-04)
mat.add_element('Cu', 9.8097e-04)
mats.append(mat)

mats.export_to_xml()
