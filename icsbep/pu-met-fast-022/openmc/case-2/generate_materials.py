import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('atom/b-cm', 0.04178839)
mat.add_nuclide('Pu239', 0.036623)
mat.add_nuclide('Pu240', 0.00066951)
mat.add_nuclide('Ga69', 0.0013211)
mat.add_nuclide('Ga71', 0.00087679)
mat.add_nuclide('Fe54', 8.3274e-06)
mat.add_nuclide('Fe56', 0.00013072)
mat.add_nuclide('Fe57', 3.0189e-06)
mat.add_nuclide('Fe58', 4.0177e-07)
mat.add_element('C', 0.00029311)
mat.add_nuclide('Ni58', 0.0012679)
mat.add_nuclide('Ni60', 0.00048838)
mat.add_nuclide('Ni61', 2.1229e-05)
mat.add_nuclide('Ni62', 6.7689e-05)
mat.add_nuclide('Ni64', 1.7238e-05)

mats.append(mat)

mats.export_to_xml()