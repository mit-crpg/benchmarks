import openmc

water = openmc.Material(name="Water with 1032.5 PPM Boron")
water.add_nuclide('H1', 6.6737e-02)
water.add_nuclide('O16', 3.3369e-02)
water.add_nuclide('B10', 1.1459e-05)
water.add_nuclide('B11', 4.6122e-05)
water.add_s_alpha_beta('c_H_in_H2O')

fuel = openmc.Material(name="Fuel (2.459 w/o with B-10 for impurities)")
fuel.add_nuclide('U234', 4.5689e-06)
fuel.add_nuclide('U235', 5.6868e-04)
fuel.add_nuclide('U238', 2.2268e-02)
fuel.add_nuclide('O16', 4.5683e-02)
fuel.add_nuclide('B10', 2.6055e-07)

aluminum = openmc.Material(name="Aluminum 6061 Cladding for Fuel")
aluminum.add_element('Mg', 6.2072e-04)
aluminum.add_element('Al', 5.3985e-02)
aluminum.add_element('Si', 3.2230e-04)
aluminum.add_element('Ti', 4.7263e-05)
aluminum.add_element('Cr', 5.8029e-05)
aluminum.add_element('Mn', 4.1191e-05)
aluminum.add_element('Fe', 1.8910e-04)
aluminum.add_element('Cu', 5.9353e-05)
aluminum.add_element('Zn', 5.7679e-05)

pyrex = openmc.Material(name="Pyrex")
pyrex.add_nuclide('B10', 9.7491e-04)
pyrex.add_nuclide('B11', 3.9241e-03)
pyrex.add_nuclide('O16', 4.4829e-02)
pyrex.add_nuclide('Na23', 1.7444e-03)
pyrex.add_nuclide('Al27', 1.0018e-03)
pyrex.add_element('Si', 1.8306e-02)

materials = openmc.Materials([water, fuel, aluminum, pyrex])
materials.export_to_xml()
