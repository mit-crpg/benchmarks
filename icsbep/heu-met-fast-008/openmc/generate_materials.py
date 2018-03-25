import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Core, R < 9.15"
mat.set_density('sum')
mat.add_nuclide('U235', 4.1031e-02)
mat.add_nuclide('U238', 4.1021e-03)
mat.add_nuclide('U234', 5.2273e-04)
mat.add_nuclide('U236', 8.8071e-05)
mat.add_element('C', 3.8642e-04)
mat.add_element('Fe', 1.3562e-04)
mat.add_element('W', 1.2415e-05)
mat.add_element('Cu', 7.1031e-04)
mat.add_element('Ni', 3.2961e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Core, outer shell"
mat.set_density('sum')
mat.add_nuclide('U235', 4.2698e-02)
mat.add_nuclide('U238', 4.0143e-03)
mat.add_nuclide('U234', 5.3154e-04)
mat.add_nuclide('U236', 1.7489e-04)
mat.add_element('C', 1.4403e-04)
mat.add_element('Fe', 3.7972e-05)
mat.add_element('W', 6.0708e-07)
mat.add_element('Al', 5.4473e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel (pure Fe)"
mat.set_density('sum')
mat.add_element('Fe', 8.1174e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "M1 copper (pure Cu)"
mat.set_density('sum')
mat.add_element('Cu', 8.2365e-02)
mats.append(mat)

mats.export_to_xml()
