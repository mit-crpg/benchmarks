import openmc

pu = openmc.Material(name="Plutonium")
pu.add_nuclide('Pu239', 3.3930e-02)
pu.add_nuclide('Pu240', 3.5043e-03)
pu.add_nuclide('Pu241', 3.9189e-04)
pu.add_element('Ga', 2.2105e-03)
pu.add_element('C', 3.0246e-03)
pu.add_element('Fe', 3.2525e-04)
pu.add_element('W', 7.4100e-05)
pu.add_element('Ni', 1.4187e-03)

reflector = openmc.Material(name="Reflector")
reflector.add_element('Be', 1.2081e-01)
reflector.add_element('O', 8.2064e-05)
reflector.add_element('C', 1.0020e-04)
reflector.add_element('Fe', 5.0939e-05)
reflector.add_s_alpha_beta('c_Be')

steel = openmc.Material(name="Steel")
steel.add_element('Fe', 8.1174e-02)

cu = openmc.Material(name="Copper")
cu.add_element('Cu', 8.2365e-02)

materials = openmc.Materials([pu, reflector, steel, cu])
materials.export_to_xml()
