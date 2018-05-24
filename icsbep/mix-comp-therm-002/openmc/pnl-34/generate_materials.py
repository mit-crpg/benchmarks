import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "UO2-PuO2 Mixture"
mat.set_density('sum')
mat.add_nuclide('Pu238', 3.8836e-08)
mat.add_nuclide('Pu239', 3.9462e-04)
mat.add_nuclide('Pu240', 3.3206e-05)
mat.add_nuclide('Pu241', 1.6081e-06)
mat.add_nuclide('Pu242', 1.1882e-07)
mat.add_nuclide('Am241', 1.4954e-06)
mat.add_nuclide('U234', 1.2458e-06)
mat.add_nuclide('U235', 1.4886e-04)
mat.add_nuclide('U236', 2.0936e-09)
mat.add_nuclide('U238', 2.0611e-02)
mat.add_nuclide('O16', 4.3779e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Natural UO2 Layer"
mat.set_density('sum')
mat.add_nuclide('U234', 1.2406e-06)
mat.add_nuclide('U235', 1.4824e-04)
mat.add_nuclide('U236', 2.0848e-09)
mat.add_nuclide('U238', 2.0525e-02)
mat.add_nuclide('O16', 4.1943e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Cladding"
mat.set_density('sum')
mat.add_element('Sn', 4.8328e-04)
mat.add_element('Fe', 9.5642e-05)
mat.add_element('Cr', 7.6093e-05)
mat.add_element('Ni', 3.0336e-05)
mat.add_element('Zr', 4.2621e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Moderator"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6706e-02)
mat.add_element('O', 3.3353e-02)
mat.add_nuclide('B10', 1.7606e-08)
mat.add_nuclide('B11', 7.1313e-08)
mat.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat)

mat = openmc.Material(5)
mat.name = "6061 Aluminum"
mat.set_density('sum')
mat.add_element('Si', 3.4607e-04)
mat.add_element('Fe', 1.0152e-04)
mat.add_element('Cu', 6.3731e-05)
mat.add_element('Mn', 2.2115e-05)
mat.add_element('Mg', 6.6651e-04)
mat.add_element('Cr', 6.2310e-05)
mat.add_element('Zn', 3.0967e-05)
mat.add_element('Ti', 2.5375e-05)
mat.add_element('Al', 5.8433e-02)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Lead"
mat.set_density('sum')
mat.add_element('Pb', 3.2174e-02)
mats.append(mat)

mats.export_to_xml()
