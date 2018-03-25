import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU, Layer 1"
mat.set_density('sum')
mat.add_nuclide('U234', 4.6992e-04)
mat.add_nuclide('U235', 4.1441e-02)
mat.add_nuclide('U238', 4.2953e-03)
mat.add_element('Cu', 7.3933e-04)
mat.add_element('C', 5.4396e-04)
mat.add_element('Ni', 5.3510e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "HEU, Layer 2"
mat.set_density('sum')
mat.add_nuclide('U234', 4.7441e-04)
mat.add_nuclide('U235', 4.1478e-02)
mat.add_nuclide('U238', 4.2390e-03)
mat.add_element('Cu', 7.4815e-04)
mat.add_element('C', 5.4378e-04)
mat.add_element('Ni', 5.9549e-04)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "HEU, Layer 3"
mat.set_density('sum')
mat.add_nuclide('U234', 4.6924e-04)
mat.add_nuclide('U235', 4.0925e-02)
mat.add_nuclide('U238', 4.2922e-03)
mat.add_element('Cu', 9.2744e-04)
mat.add_element('C', 5.3785e-04)
mat.add_element('Ni', 6.7552e-04)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "HEU, Layer 4"
mat.set_density('sum')
mat.add_nuclide('U234', 5.2726e-04)
mat.add_nuclide('U235', 4.1135e-02)
mat.add_nuclide('U238', 4.2744e-03)
mat.add_element('Cu', 8.6198e-04)
mat.add_element('C', 5.4074e-04)
mat.add_element('Ni', 4.3585e-04)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "HEU, Layer 5"
mat.set_density('sum')
mat.add_nuclide('U234', 4.8840e-04)
mat.add_nuclide('U235', 4.1062e-02)
mat.add_nuclide('U238', 4.2174e-03)
mat.add_element('Cu', 8.3777e-04)
mat.add_element('C', 4.4891e-04)
mat.add_element('Ni', 4.9452e-04)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "HEU, Layer 6"
mat.set_density('sum')
mat.add_nuclide('U234', 5.0504e-04)
mat.add_nuclide('U235', 4.1306e-02)
mat.add_nuclide('U238', 4.2137e-03)
mat.add_element('Cu', 8.0432e-04)
mat.add_element('C', 3.6114e-04)
mat.add_element('Ni', 5.5572e-04)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "HEU, Layer 7"
mat.set_density('sum')
mat.add_nuclide('U234', 4.8000e-04)
mat.add_nuclide('U235', 4.1191e-02)
mat.add_nuclide('U238', 4.1791e-03)
mat.add_element('Cu', 6.3602e-04)
mat.add_element('C', 3.5973e-04)
mat.add_element('Ni', 3.5410e-04)
mats.append(mat)

mat = openmc.Material(8)
mat.name = "Depleted uranium, Layer 1"
mat.set_density('sum')
mat.add_nuclide('U235', 2.1044e-04)
mat.add_nuclide('U238', 4.6780e-02)
mat.add_element('C', 2.9015e-03)
mat.add_element('Fe', 3.8246e-04)
mats.append(mat)

mat = openmc.Material(9)
mat.name = "Depleted uranium, Layer 2"
mat.set_density('sum')
mat.add_nuclide('U235', 2.1047e-04)
mat.add_nuclide('U238', 4.6786e-02)
mat.add_element('C', 2.9018e-03)
mat.add_element('Fe', 3.8251e-04)
mats.append(mat)

mat = openmc.Material(10)
mat.name = "Depleted uranium, Layer 3"
mat.set_density('sum')
mat.add_nuclide('U235', 2.1912e-04)
mat.add_nuclide('U238', 4.5586e-02)
mat.add_element('C', 2.8282e-03)
mat.add_element('Fe', 3.7281e-04)
mats.append(mat)

mat = openmc.Material(11)
mat.name = "Depleted uranium, Layer 4"
mat.set_density('sum')
mat.add_nuclide('U235', 2.1059e-04)
mat.add_nuclide('U238', 4.5767e-02)
mat.add_element('C', 2.8389e-03)
mat.add_element('Fe', 3.7422e-04)
mats.append(mat)

mats.export_to_xml()
