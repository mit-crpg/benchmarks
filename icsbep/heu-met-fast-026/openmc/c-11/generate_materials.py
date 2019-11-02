import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "HEU"
mat.set_density('sum')
mat.add_nuclide('U234', 4.8271e-04)
mat.add_nuclide('U235', 4.4797e-02)
mat.add_nuclide('U236', 9.5723e-05)
mat.add_nuclide('U238', 2.6577e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Stainless Steel"
mat.set_density('sum')
mat.add_element('C', 3.1691e-04)
mat.add_element('Mn', 1.7321e-03)
mat.add_element('Si', 1.6940e-03)
mat.add_element('Cr', 1.6472e-02)
mat.add_element('Fe', 6.0360e-02)
mat.add_element('Ni', 6.4834e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Concrete"
mat.set_density('sum')
mat.add_element('H', 1.4868e-02)
mat.add_element('C', 3.8144e-03)
mat.add_element('O', 4.1519e-02)
mat.add_element('Na', 3.0400e-04)
mat.add_element('Mg', 5.8700e-04)
mat.add_element('Al', 7.3500e-04)
mat.add_element('Si', 6.0370e-03)
mat.add_element('Ca', 1.1588e-02)
mat.add_element('Fe', 1.9680e-04)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Paraffin"
mat.set_density('sum')
mat.add_nuclide('H1', 8.2574e-02)
mat.add_element('C', 3.9699e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mats.export_to_xml()
