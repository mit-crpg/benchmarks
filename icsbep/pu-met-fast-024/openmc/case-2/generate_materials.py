import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "98% Pu-239 in delta phase"
mat.set_density('atom/b-cm', 0.04189142)
mat.add_nuclide('Pu239', 0.03662)
mat.add_nuclide('Pu240', 0.00066944)
mat.add_nuclide('Ga69', 0.001320091896)
mat.add_nuclide('Ga71', 0.000876108104)
mat.add_nuclide('Fe54', 8.256647e-06)
mat.add_nuclide('Fe56', 0.0001296117004)
mat.add_nuclide('Fe57', 2.9932994e-06)
mat.add_nuclide('Fe58', 3.983532e-07)
mat.add_element('C', 0.00028972)
mat.add_nuclide('Ni58', 0.0013443826212)
mat.add_nuclide('Ni60', 0.0005178537788)
mat.add_nuclide('Ni61', 2.25107452e-05)
mat.add_nuclide('Ni62', 7.1774106e-05)
mat.add_nuclide('Ni64', 1.82787488e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Polyethylene"
mat.set_density('atom/b-cm', 0.116442)
mat.add_nuclide('H1', 0.077628)
mat.add_element('C', 0.038814)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mats.export_to_xml()