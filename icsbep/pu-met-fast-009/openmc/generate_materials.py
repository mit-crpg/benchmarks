import openmc

core = openmc.Material(name='Core')
core.add_nuclide('Pu239', 3.7592e-02)
core.add_nuclide('Pu240', 1.9349e-03)
core.add_nuclide('Pu241', 1.1797e-04)
core.add_element('Ga', 1.3733e-03)

reflector = openmc.Material(name='Reflector')
reflector.add_element('Al', 5.8787e-02)
reflector.add_element('Cu', 1.1759e-03)
reflector.add_element('Si', 2.4187e-04)
reflector.add_element('Mn', 2.4729e-04)
reflector.add_element('Mg', 3.4936e-04)

materials = openmc.Materials([core, reflector])
materials.export_to_xml()
