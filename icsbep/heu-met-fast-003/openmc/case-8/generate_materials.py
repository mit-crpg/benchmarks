import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Oralloy"
mat.set_density('sum')
mat.add_nuclide('U234', 4.9210e-04)
mat.add_nuclide('U235', 4.4917e-02)
mat.add_nuclide('U238', 2.5993e-03)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Tungsten carbide"
mat.set_density('sum')
mat.add_nuclide('W182', 1.2697e-02)
mat.add_nuclide('W183', 6.8626e-03)
mat.add_nuclide('W184', 1.4754e-02)
mat.add_nuclide('W186', 1.3744e-02)
mat.add_element('C', 4.8057e-02)
mats.append(mat)

mats.export_to_xml()
