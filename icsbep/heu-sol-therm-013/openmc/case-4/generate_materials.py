import openmc

un = openmc.Material(name="Uranium Nitrate Solution")
un.add_nuclide('U234', 7.6139e-07)
un.add_nuclide('U235', 6.7926e-05)
un.add_nuclide('U236', 1.9599e-07)
un.add_nuclide('U238', 3.9659e-06)
un.add_element('N', 2.5463e-04)
un.add_nuclide('B10', 2.5472e-06)
un.add_nuclide('B11', 1.0253e-05)
un.add_element('O', 3.3844e-02)
un.add_nuclide('H1', 6.5964e-02)
un.add_s_alpha_beta('c_H_in_H2O')

aluminum = openmc.Material(name="Type 1100 Aluminum")
aluminum.add_element('Al', 5.9699e-02)
aluminum.add_element('Si', 5.5202e-04)
aluminum.add_element('Cu', 5.1364e-05)
aluminum.add_element('Zn', 2.4958e-05)
aluminum.add_element('Mn', 1.4853e-05)

materials = openmc.Materials([un, aluminum])
materials.export_to_xml()
