import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU, Layer 1"
mat.set_density('sum')
mat.add_nuclide('U234', 5.0708e-04)
mat.add_nuclide('U235', 4.1828e-02)
mat.add_nuclide('U238', 4.2699e-03)
mat.add_element('C', 7.3190e-04)
mat.add_element('Fe', 1.1806e-04)
mat.add_element('W', 3.5862e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "HEU, Layer 2"
mat.set_density('sum')
mat.add_nuclide('U234', 5.0050e-04)
mat.add_nuclide('U235', 4.1658e-02)
mat.add_nuclide('U238', 4.1803e-03)
mat.add_element('C', 1.4583e-03)
mat.add_element('Fe', 2.3523e-04)
mat.add_element('W', 7.1455e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "HEU, Layer 3"
mat.set_density('sum')
mat.add_nuclide('U234', 5.3263e-04)
mat.add_nuclide('U235', 4.1312e-02)
mat.add_nuclide('U238', 4.4603e-03)
mat.add_element('C', 1.2746e-03)
mat.add_element('Fe', 2.1538e-04)
mat.add_element('W', 5.9477e-05)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "HEU, Layer 4"
mat.set_density('sum')
mat.add_nuclide('U234', 5.3885e-04)
mat.add_nuclide('U235', 4.1823e-02)
mat.add_nuclide('U238', 4.5031e-03)
mat.add_element('C', 1.1052e-03)
mat.add_element('Fe', 1.9809e-04)
mat.add_element('W', 5.4154e-05)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "HEU, Layer 5"
mat.set_density('sum')
mat.add_nuclide('U234', 5.4361e-04)
mat.add_nuclide('U235', 4.1769e-02)
mat.add_nuclide('U238', 4.5313e-03)
mat.add_element('C', 1.2895e-03)
mat.add_element('Fe', 2.1791e-04)
mat.add_element('W', 6.6193e-05)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "HEU, Layer 6"
mat.set_density('sum')
mat.add_nuclide('U234', 5.1940e-04)
mat.add_nuclide('U235', 4.2390e-02)
mat.add_nuclide('U238', 4.3476e-03)
mat.add_element('C', 1.0214e-03)
mat.add_element('Fe', 1.7973e-04)
mat.add_element('W', 5.4595e-05)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "HEU, Layer 7"
mat.set_density('sum')
mat.add_nuclide('U234', 5.1956e-04)
mat.add_nuclide('U235', 4.2360e-02)
mat.add_nuclide('U238', 4.3676e-03)
mat.add_element('C', 1.2074e-03)
mat.add_element('Fe', 2.1973e-04)
mat.add_element('W', 6.0679e-05)
mats.append(mat)

mat = openmc.Material(8)
mat.name = "HEU, Layer 8"
mat.set_density('sum')
mat.add_nuclide('U234', 5.1351e-04)
mat.add_nuclide('U235', 4.2363e-02)
mat.add_nuclide('U238', 4.3006e-03)
mat.add_element('C', 8.3383e-04)
mat.add_element('Fe', 1.5941e-04)
mat.add_element('W', 4.2369e-05)
mats.append(mat)

mat = openmc.Material(9)
mat.name = "HEU, Layer 9"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2352e-04)
mat.add_nuclide('U235', 4.2309e-02)
mat.add_nuclide('U238', 4.3843e-03)
mat.add_element('C', 9.2736e-04)
mat.add_element('Fe', 1.5956e-04)
mat.add_element('W', 4.2409e-05)
mats.append(mat)

mat = openmc.Material(10)
mat.name = "Lead"
mat.set_density('sum')
mat.add_element('Pb', 3.2838e-02)
mat.add_element('Fe', 1.8399e-05)
mats.append(mat)

mats.export_to_xml()
