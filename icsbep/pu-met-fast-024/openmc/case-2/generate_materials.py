import openmc

pu = openmc.Material(name = "98% Pu-239 in delta phase")
pu.add_nuclide('Pu239', 3.6620e-02)
pu.add_nuclide('Pu240', 6.6944e-04)
pu.add_element('Ga', 2.1962e-03)
pu.add_element('Fe', 1.4126e-04)
pu.add_element('C', 2.8972e-04)
pu.add_element('Ni', 1.9748e-03)

ch2 = openmc.Material(name="Polyethylene")
ch2.add_element('C', 0.038814)
ch2.add_nuclide('H1', 0.077628)
ch2.add_s_alpha_beta('c_H_in_CH2')

materials = openmc.Materials([pu, ch2])
materials.export_to_xml()
