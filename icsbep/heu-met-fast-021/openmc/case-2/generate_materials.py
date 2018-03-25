import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2087e-04)
mat.add_nuclide('U235', 4.2023e-02)
mat.add_nuclide('U238', 4.3613e-03)
mat.add_element('C', 1.0919e-03)
mat.add_element('Fe', 1.9435e-04)
mat.add_element('W', 5.5050e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Steel reflector 1"
mat.set_density('sum')
mat.add_element('Fe', 7.9417e-02)
mat.add_element('C', 1.1269e-03)
mat.add_element('Si', 1.6065e-04)
mat.add_element('Cr', 2.6032e-04)
mat.add_element('Mn', 3.2851e-04)
mat.add_element('Ni', 2.3063e-04)
mat.add_element('Cu', 2.1301e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel reflector 2"
mat.set_density('sum')
mat.add_element('Fe', 7.9045e-02)
mat.add_element('C', 1.1217e-03)
mat.add_element('Si', 1.5990e-04)
mat.add_element('Cr', 2.5910e-04)
mat.add_element('Mn', 3.2697e-04)
mat.add_element('Ni', 2.2955e-04)
mat.add_element('Cu', 2.1201e-04)
mats.append(mat)

mats.export_to_xml()
