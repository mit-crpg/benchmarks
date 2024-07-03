import openmc

solution = openmc.Material(name="IEU Flouride Solution")
solution.add_nuclide('U232', 4.5608e-08)
solution.add_nuclide('U233', 2.2379e-03)
solution.add_nuclide('U234', 2.4316e-05)
solution.add_nuclide('U235', 8.9598e-07)
solution.add_nuclide('U238', 7.1284e-06)
solution.add_nuclide('H1', 5.5183e-02)
solution.add_element('O', 3.2043e-02)
solution.add_element('F', 4.7182e-03)
solution.add_s_alpha_beta('c_H_in_H2O')

steel = openmc.Material(name="347 Stainless steel")
steel.add_element('Fe', 6.1248e-02)
steel.add_element('Cr', 1.6678e-02)
steel.add_element('Ni', 9.0264e-03)

reflector = openmc.Material(name="Beryllium reflector")
reflector.add_element('Be', 1.2161e-01)
reflector.add_s_alpha_beta('c_Be')

materials = openmc.Materials([solution, steel, reflector])
materials.export_to_xml()
