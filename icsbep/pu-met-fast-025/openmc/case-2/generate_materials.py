import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6704e-02)
mat.add_nuclide('Pu240', 6.7099e-04)
mat.add_element('Ga', 2.2013e-03)
mat.add_element('Fe', 1.4159e-04)
mat.add_element('C', 2.9038e-04)
mat.add_element('Ni', 1.9794e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Steel reflector"
mat.set_density('sum')
mat.add_element('Fe', 7.9557e-02)
mat.add_element('C', 1.1289e-03)
mat.add_element('Si', 1.6093e-04)
mat.add_element('Cr', 2.6078e-04)
mat.add_element('Mn', 3.2909e-04)
mat.add_element('Ni', 2.3104e-04)
mat.add_element('Cu', 2.1338e-04)
mats.append(mat)

mats.export_to_xml()
