import openmc

inner = openmc.Material(name="U233 Inner Sphere")
inner.add_nuclide('U233', 4.7312e-02)
inner.add_nuclide('U235', 5.2770e-04)
inner.add_nuclide('U238', 3.3015e-04)

outer = openmc.Material(name = "U235 Outer Shell")
outer.add_nuclide('U235', 4.4892e-02)
outer.add_nuclide('U238', 3.2340e-03)

materials = openmc.Materials([inner, outer])
materials.export_to_xml()
