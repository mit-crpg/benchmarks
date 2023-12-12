import openmc

mats = openmc.Materials()

mat1 = openmc.Material(1)
mat1.name = "Water with 1511 PPM"
mat1.set_density('atom/b-cm', 0.10019)
mat1.add_nuclide('H1', 6.6737e-02)
mat1.add_nuclide('O16', 3.3369e-02)
mat1.add_nuclide('B10', 1.6769e-05)
mat1.add_nuclide('B11', 6.7497e-05)
mat1.add_s_alpha_beta('c_H_in_H2O')
mats.append(mat1)

mat2 = openmc.Material(2)
mat2.name = "Fuel (2.459 w/o with B-10 for impurities)"
mat2.set_density('atom/b-cm', 0.068525)
mat2.add_nuclide('U234', 4.5689e-06)
mat2.add_nuclide('U235', 5.6868e-04)
mat2.add_nuclide('U238', 2.2268e-02)
mat2.add_nuclide('O16', 4.5683e-02)
mat2.add_nuclide('B10', 2.6055e-07)
mats.append(mat2)

mat3 = openmc.Material(3)
mat3.name = "Aluminum 6061 Cladding for Fuel"
mat3.set_density('atom/b-cm', 0.055323)
mat3.add_nuclide('Mg24', 4.9031e-04)
mat3.add_nuclide('Mg25',6.2072e-05)
mat3.add_nuclide('Mg26', 6.8341e-05)

mat3.add_nuclide('Al27', 5.3985e-02)

mat3.add_nuclide('Si28', 2.9726e-04)
mat3.add_nuclide('Si29', 1.5094e-05)
mat3.add_nuclide('Si30', 9.9499e-06)

mat3.add_nuclide('Ti46', 3.8992e-06)
mat3.add_nuclide('Ti47', 3.5164e-06)
mat3.add_nuclide('Ti48', 3.4842e-05)
mat3.add_nuclide('Ti49', 2.5569e-06)
mat3.add_nuclide('Ti50', 2.4482e-06)

mat3.add_nuclide('Cr50', 2.5214e-06)
mat3.add_nuclide('Cr52', 4.8622e-05)
mat3.add_nuclide('Cr53', 5.5133e-06)
mat3.add_nuclide('Cr54', 1.3724e-06)

mat3.add_nuclide('Mn55',4.1191e-05)

mat3.add_nuclide('Fe54', 1.1053e-05)
mat3.add_nuclide('Fe56', 1.7351e-04)
mat3.add_nuclide('Fe57', 4.0070e-06)
mat3.add_nuclide('Fe58', 5.3326e-07)

mat3.add_nuclide('Cu63', 4.1054e-05)
mat3.add_nuclide('Cu65', 1.8299e-05)
   
mat3.add_nuclide('Zn64', 2.8361e-05)
mat3.add_nuclide('Zn66', 1.5994e-05)
mat3.add_nuclide('Zn67', 2.3302e-06)
mat3.add_nuclide('Zn68', 1.0642e-05)
mat3.add_nuclide('Zn70', 3.5184e-07)
mats.append(mat3)

mats.export_to_xml()