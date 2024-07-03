import openmc

un = openmc.Material(name="Uranyl Nitrate Solution")
un.add_nuclide('U234', 5.9840e-07)
un.add_nuclide('U235', 7.4257e-05)
un.add_nuclide('U236', 7.4165e-08)
un.add_nuclide('U238', 6.6142e-04)
un.add_nuclide('H1', 5.7176e-02)
un.add_element('N', 2.8156e-03)
un.add_element('O', 3.7836e-02)
un.add_s_alpha_beta('c_H_in_H2O')

steel = openmc.Material(name="Stainless Steel")
steel.add_element('C', 4.3736e-05)
steel.add_element('Si', 1.0627e-03)
steel.add_element('Mn', 1.1561e-03)
steel.add_element('P', 4.3170e-05)
steel.add_element('S', 2.9782e-06)
steel.add_element('Ni', 8.3403e-03)
steel.add_element('Cr', 1.6775e-02)
steel.add_element('Fe', 5.9421e-02)

air = openmc.Material(name="Air")
air.add_element('N', 3.9016e-05)
air.add_element('O', 1.0409e-05)

materials = openmc.Materials([un, steel, air])
materials.export_to_xml()
