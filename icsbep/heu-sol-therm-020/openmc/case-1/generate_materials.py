import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "UO2F2/D2O Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 3.0660e-06)
mat.add_nuclide('U235', 2.8020e-04)
mat.add_nuclide('U238', 1.5751e-05)
mat.add_element('F', 5.9823e-04)
mat.add_element('O', 3.2832e-02)
mat.add_nuclide('H2', 6.3823e-02)
mat.add_nuclide('H1', 6.4468e-04)
mat.add_s_alpha_beta('c_D_in_D2O')
mats.append(mat)

mat = openmc.Material(2)
mat.name = "321 Stainless Steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9355e-02)
mat.add_element('Cr', 1.6511e-02)
mat.add_element('Ni', 7.7203e-03)
mat.add_element('Mn', 1.7363e-03)
mat.add_element('Si', 1.6982e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Dry Air"
mat.set_density('sum')
mat.add_element('N', 3.2269e-05)
mat.add_element('O', 8.6569e-06)
mats.append(mat)

mats.export_to_xml()
