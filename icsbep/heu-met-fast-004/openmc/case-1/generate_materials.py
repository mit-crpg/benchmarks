import openmc

oralloy = openmc.Material(name="Oralloy")
oralloy.add_nuclide("U234", 5.3678e-4)
oralloy.add_nuclide("U235", 4.7033e-2)
oralloy.add_nuclide("U236", 9.5896e-5)
oralloy.add_nuclide("U238", 4.7782e-4)

lucite = openmc.Material(name="Lucite")
lucite.add_nuclide("H1", 5.7745e-2)
lucite.add_element("C", 3.6090e-2)
lucite.add_nuclide("O16", 1.4435e-2)
lucite.add_s_alpha_beta("c_H_in_H2O")

water = openmc.Material(name="Water")
water.add_nuclide("H1", 6.6807e-2)
water.add_nuclide("O16", 3.3403e-2)
water.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([oralloy, lucite, water])
materials.export_to_xml()
