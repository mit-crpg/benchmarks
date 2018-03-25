import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "36 wt% U-235"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5511e-04)
mat.add_nuclide('U235', 1.7154e-02)
mat.add_nuclide('U238', 2.9297e-02)
mat.add_element('W', 1.0711e-05)
mat.add_element('Fe', 1.2324e-04)
mat.add_element('C', 6.4945e-04)
mat.add_element('Cu', 2.6791e-04)
mat.add_element('Ni', 2.9008e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Steel reflector #1"
mat.set_density('sum')
mat.add_element('Fe', 7.9285e-02)
mat.add_element('C', 1.1251e-03)
mat.add_element('Si', 1.6038e-04)
mat.add_element('Cr', 2.5989e-04)
mat.add_element('Mn', 3.2796e-04)
mat.add_element('Ni', 2.3025e-04)
mat.add_element('Cu', 2.1265e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Steel reflector #2"
mat.set_density('sum')
mat.add_element('Fe', 8.0388e-02)
mat.add_element('C', 1.1407e-03)
mat.add_element('Si', 1.6261e-04)
mat.add_element('Cr', 2.6351e-04)
mat.add_element('Mn', 3.3253e-04)
mat.add_element('Ni', 2.3345e-04)
mat.add_element('Cu', 2.1561e-04)
mats.append(mat)

mats.export_to_xml()
