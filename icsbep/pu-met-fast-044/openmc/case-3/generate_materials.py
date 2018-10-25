import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium-Gallium alloy"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.7028e-02)
mat.add_nuclide('Pu240', 1.9931e-03)
mat.add_nuclide('Pu240', 1.3594e-04)
mat.add_element('Ga', 1.2880e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Nickel coating"
mat.set_density('sum')
mat.add_element('Ni', 1.2962e-01)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Air"
mat.set_density('sum')
mat.add_element('N', 3.9933e-05)
mat.add_element('O', 8.7399e-06)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Tamper"
mat.set_density('sum')
mat.add_element('Be', 1.2199e-01)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Polyethylene"
mat.set_density('sum')
mat.add_element('C', 3.9756e-02)
mat.add_element('H', 7.9512e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mats.export_to_xml()
