import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "36 wt% U-235, Layer 1"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5922e-04)
mat.add_nuclide('U235', 1.7440e-02)
mat.add_nuclide('U238', 2.9990e-02)
mat.add_element('C', 4.7009e-04)
mat.add_element('Fe', 1.6176e-04)
mat.add_element('W', 1.2284e-05)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "36 wt% U-235, Layer 2"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5878e-04)
mat.add_nuclide('U235', 1.7415e-02)
mat.add_nuclide('U238', 2.9887e-02)
mat.add_element('C', 3.7502e-04)
mat.add_element('Fe', 1.6131e-04)
mat.add_element('W', 1.2250e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "36 wt% U-235, Layer 3"
mat.set_density('sum')
mat.add_nuclide('U234', 1.5803e-04)
mat.add_nuclide('U235', 1.7418e-02)
mat.add_nuclide('U238', 2.9651e-02)
mat.add_element('C', 5.5986e-04)
mat.add_element('Fe', 1.6054e-04)
mat.add_element('W', 1.2192e-05)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "36 wt% U-235, Layer 4"
mat.set_density('sum')
mat.add_nuclide('U234', 1.3423e-04)
mat.add_nuclide('U235', 1.7356e-02)
mat.add_nuclide('U238', 2.9786e-02)
mat.add_element('C', 7.4727e-04)
mat.add_element('Fe', 1.2054e-04)
mat.add_element('W', 1.2205e-05)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "36 wt% U-235, Layer 5"
mat.set_density('sum')
mat.add_nuclide('U234', 1.6281e-04)
mat.add_nuclide('U235', 1.7417e-02)
mat.add_nuclide('U238', 2.9663e-02)
mat.add_element('C', 5.5983e-04)
mat.add_element('Fe', 1.0034e-04)
mat.add_element('W', 6.0956e-06)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Polyethylene, Layer 1"
mat.set_density('sum')
mat.add_nuclide('H1', 7.5542e-02)
mat.add_element('C', 3.7771e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Polyethylene, Layer 2"
mat.set_density('sum')
mat.add_nuclide('H1', 7.4170e-02)
mat.add_element('C', 3.7085e-02)
mat.add_s_alpha_beta('c_H_in_CH2')
mats.append(mat)

mats.export_to_xml()
