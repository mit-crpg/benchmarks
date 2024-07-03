import openmc

pu = openmc.Material(name = "98% Pu-239 in delta phase")
pu.add_nuclide('Pu239', 3.6623e-02)
pu.add_nuclide('Pu240', 6.6951e-04)
pu.add_element('Ga', 2.1979e-03)
pu.add_element('Fe', 1.4247e-04)
pu.add_element('C', 2.9311e-04)
pu.add_element('Ni', 1.8624e-03)

materials = openmc.Materials([pu])
materials.export_to_xml()
