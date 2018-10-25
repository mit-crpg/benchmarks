import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Layer 1"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.5932e-02)
mat.add_nuclide('Pu240', 6.5685e-04)
mat.add_element('Ga', 2.2615e-03)
mat.add_element('C', 2.9667e-04)
mat.add_element('Ni', 4.2235e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Layer 2"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6826e-02)
mat.add_nuclide('Pu240', 6.7320e-04)
mat.add_element('Ga', 2.3178e-03)
mat.add_element('C', 3.0406e-04)
mat.add_element('Ni', 1.5722e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Layer 3"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6579e-02)
mat.add_nuclide('Pu240', 6.6875e-04)
mat.add_element('Ga', 2.3155e-03)
mat.add_element('C', 3.0205e-04)
mat.add_element('Ni', 1.9330e-03)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Layer 4"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6512e-02)
mat.add_nuclide('Pu240', 6.6739e-04)
mat.add_element('Ga', 2.2978e-03)
mat.add_element('C', 2.2608e-04)
mat.add_element('Ni', 2.3056e-03)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Layer 5"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6576e-02)
mat.add_nuclide('Pu240', 6.6878e-04)
mat.add_element('Ga', 2.3286e-03)
mat.add_element('C', 3.0206e-04)
mat.add_element('Ni', 1.8631e-03)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Layer 6"
mat.set_density('sum')
mat.add_nuclide('Pu239', 3.6471e-02)
mat.add_nuclide('Pu240', 6.6665e-04)
mat.add_element('Ga', 2.2823e-03)
mat.add_element('C', 3.0110e-04)
mat.add_element('Ni', 1.9715e-03)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Cadmium reflector"
mat.set_density('sum')
mat.add_element('Cd', 4.6340e-02)
mats.append(mat)

mat = openmc.Material(8)
mat.name = "Polyethlyene reflector, layer 1"
mat.set_density('sum')
mat.add_element('H', 7.3845e-02)
mat.add_element('C', 3.6922e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mat = openmc.Material(9)
mat.name = "Polyethlyene reflector, layer 2"
mat.set_density('sum')
mat.add_element('H', 7.8997e-02)
mat.add_element('C', 3.9498e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mat = openmc.Material(10)
mat.name = "Polyethlyene reflector, layer 3"
mat.set_density('sum')
mat.add_element('H', 7.8996e-02)
mat.add_element('C', 3.9498e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mats.export_to_xml()
