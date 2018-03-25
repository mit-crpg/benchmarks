import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "36 wt% U-235"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5272e-04)
mat.add_nuclide('U235', 1.7118e-02)
mat.add_nuclide('U238', 2.9211e-02)
mat.add_element('C', 7.7389e-04)
mat.add_element('Fe', 1.2058e-04)
mat.add_element('W', 1.0087e-05)
mat.add_element('Cu', 3.8133e-04)
mat.add_element('Ni', 4.1288e-04)
mats.append(mat)

mats.export_to_xml()
