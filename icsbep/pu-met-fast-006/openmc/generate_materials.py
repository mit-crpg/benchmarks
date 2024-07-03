import openmc

core = openmc.Material(name='Core')
core.add_nuclide('Pu239', 3.6697e-02)
core.add_nuclide('Pu240', 1.8700e-03)
core.add_nuclide('Pu241', 1.1639e-04)
core.add_element('Ga', 1.4755e-03)

reflector = openmc.Material(name='Reflector')
reflector.add_nuclide('U234', 2.6438e-06)
reflector.add_nuclide('U235', 3.4610e-04)
reflector.add_nuclide('U238', 4.7721e-02)

materials = openmc.Materials([core, reflector])
materials.export_to_xml()
