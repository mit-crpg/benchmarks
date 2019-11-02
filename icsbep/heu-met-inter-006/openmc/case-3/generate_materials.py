import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 4.9568e-04)
mat.add_nuclide('U235', 4.4930e-02)
mat.add_nuclide('U236', 1.5647e-04)
mat.add_nuclide('U238', 2.5757e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "c_Graphite"
mat.set_density('sum')
mat.add_element('C', 8.6431e-02)
mat.add_s_alpha_beta('c_Graphite')
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Cu"
mat.set_density('sum')
mat.add_element('Cu', 8.2780e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Al 6061-T6"
mat.set_density('sum')
mat.add_element('Si', 3.4295e-04)
mat.add_element('Fe', 1.0061e-04)
mat.add_element('Cu', 6.9471e-05)
mat.add_element('Mn', 2.1915e-05)
mat.add_element('Mg', 6.6049e-04)
mat.add_element('Cr', 7.7185e-05)
mat.add_element('Zn', 3.0687e-05)
mat.add_element('Ti', 2.5146e-05)
mat.add_element('Al', 5.7816e-02)
mats.append(mat)

mats.export_to_xml()
