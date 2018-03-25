import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.set_density('sum')
mat.add_nuclide('U233', 4.7312e-2)
mat.add_nuclide('U234', 5.2770e-4)
mat.add_nuclide('U238', 3.3015e-4)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Tungsten reflector"
mat.set_density('sum')
mat.add_element('W', 5.1468e-02)
mat.add_element('Ni', 9.7124e-03)
mat.add_element('Cu', 4.0774e-03)
mat.add_element('Zr', 7.9528e-04)
mats.append(mat)

mats.export_to_xml()
