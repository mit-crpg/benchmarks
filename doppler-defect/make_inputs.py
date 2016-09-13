#!/usr/bin/env python

import os
import openmc


# ==============================================================================
# PHYSICAL DATA FOR MOSTELLER DOPPLER BENCHMARK

enrichments = {'uo2': [0.711, 1.6, 2.4, 3.1, 3.9, 4.5, 5.0],
               'reactor-mox': [1.0, 2.0, 4.0, 6.0, 8.0],
               'weapons-mox': [1.0, 2.0, 4.0, 6.0]}

fuel_or = {300: 0.39306, 600: 0.39398, 900: 0.39433}
clad_ir = {300: 0.40077, 600: 0.40226, 900: 0.40226}
clad_or = {300: 0.45802, 600: 0.45972, 900: 0.45972}
pitch = {300: 1.26209, 600: 1.26678, 900: 1.26678}

clad_density = {600: 0.0421838}

water_comp = {600: [('H1', 4.42326e-2),
                    ('B10', 1.02133e-5),
                    ('B11', 4.11098e-5),
                    ('O16', 2.21163e-2)]}

composition = {
    'uo2': {
        'nuclides': ['O16', 'U234', 'U235', 'U238'],
        'densities': {
            600: {0.711: [4.61171e-2, 0, 1.66029e-4, 2.28925e-2],
                  1.6: [4.61218e-2, 3.00175e-6, 3.73618e-4, 2.26843e-2],
                  2.4: [4.61260e-2, 4.50257e-6, 5.60420e-4, 2.24981e-2],
                  3.1: [4.61297e-2, 5.81576e-6, 7.23867e-4, 2.23352e-2],
                  3.9: [4.61339e-2, 7.31651e-6, 9.10661e-4, 2.21490e-2],
                  4.5: [4.61371e-2, 8.44205e-6, 1.05075e-3, 2.20093e-2],
                  5.0: [4.61397e-2, 9.37998e-6, 1.16749e-3, 2.18930e-2]},
            900: {0.711: [4.59967e-2, 0, 1.65595e-4, 2.28328e-2],
                  1.6: [4.60014e-2, 2.99391e-6, 3.72642e-4, 2.26251e-2],
                  2.4: [4.60056e-2, 4.49081e-6, 5.58956e-4, 2.24393e-2],
                  3.1: [4.60093e-2, 5.80057e-6, 7.21977e-4, 2.22768e-2],
                  3.9: [4.60134e-2, 7.29740e-6, 9.08283e-4, 2.20911e-2],
                  4.5: [4.60166e-2, 8.42000e-6, 1.04801e-3, 2.19519e-2],
                  5.0: [4.60192e-2, 9.35548e-6, 1.16445e-3, 2.18358e-2]}}},
    'reactor-mox': {
        'nuclides': ['O16', 'U235', 'U238', 'Pu239', 'Pu240', 'Pu241', 'Pu242'],
        'densities': {
            600: {
                1.0: [4.61140e-2, 1.64368e-4, 2.26636e-2, 1.03031e-4, 6.86872e-5, 3.43436e-5, 2.28957e-5],
                2.0: [4.61108e-2, 1.62708e-4, 2.24347e-2, 2.06062e-4, 1.37374e-4, 6.86872e-5, 4.57915e-5],
                4.0: [4.61042e-2, 1.59387e-4, 2.19768e-2, 4.12123e-4, 2.74749e-4, 1.37374e-4, 9.15830e-5],
                6.0: [4.60977e-2, 1.56067e-4, 2.15190e-2, 6.18185e-4, 4.12123e-4, 2.06062e-4, 1.37374e-4],
                8.0: [4.60912e-2, 1.52746e-4, 2.10611e-2, 8.24247e-4, 5.49498e-4, 2.74749e-4, 1.83166e-4]},
            900: {
                1.0: [4.59936e-2, 1.63939e-4, 2.26044e-2, 1.02762e-4, 6.85079e-5, 3.42539e-5, 2.28360e-5],
                2.0: [4.59904e-2, 1.62283e-4, 2.23761e-2, 2.05524e-4, 1.37016e-4, 6.85079e-5, 4.56719e-5],
                4.0: [4.59838e-2, 1.58971e-4, 2.19194e-2, 4.11047e-4, 2.74031e-4, 1.37016e-4, 9.13438e-5],
                6.0: [4.59773e-2, 1.55659e-4, 2.14628e-2, 6.16571e-4, 4.11047e-4, 2.05524e-4, 1.37016e-4],
                8.0: [4.59708e-2, 1.52347e-4, 2.10061e-2, 8.22094e-4, 5.48063e-4, 2.74031e-4, 1.82688e-4]}}},
    'weapons-mox': {
        'nuclides': ['O16', 'U235', 'U238', 'Pu239', 'Pu240', 'Pu241', 'Pu242'],
        'densities': {
            600: {
                1.0: [4.61154e-2, 1.64368e-4, 2.26636e-2, 2.14958e-4, 1.35497e-5, 9.18623e-7, 2.29656e-7],
                2.0: [4.61136e-2, 1.62708e-4, 2.24347e-2, 4.29916e-4, 2.70994e-5, 1.83725e-6, 4.59312e-7],
                4.0: [4.61099e-2, 1.59387e-4, 2.19768e-2, 8.59831e-4, 5.41988e-5, 3.67449e-6, 9.18623e-7],
                6.0: [4.61061e-2, 1.56067e-4, 2.15190e-2, 1.28975e-3, 8.12982e-5, 5.51174e-6, 1.37794e-6]},
            900: {
                1.0: [4.59950e-2, 1.63939e-4, 2.26044e-2, 2.14397e-4, 1.35143e-5, 9.16224e-7, 2.29656e-7],
                2.0: [4.59932e-2, 1.62283e-4, 2.23761e-2, 4.28793e-4, 2.70286e-5, 1.83245e-6, 4.58112e-7],
                4.0: [4.59895e-2, 1.58971e-4, 2.19194e-2, 8.57586e-4, 5.40572e-5, 3.66490e-6, 9.16224e-7],
                6.0: [4.59857e-2, 1.55659e-4, 2.14628e-2, 1.28638e-3, 8.10859e-5, 5.49735e-6, 1.37434e-6]}
        }
    }
}

# ==============================================================================
# CREATE MODELS USING PHYSICAL DATA

# Define simulation settings
settings = openmc.Settings()
settings.particles = 10000
settings.inactive = 20
settings.batches = 100
settings.keff_trigger = {'type': 'std_dev', 'threshold': 0.0004}
settings.trigger_max_batches = 1000
settings.trigger_active = True
settings.cross_sections = '/home/romano/openmc/data/mcnp_hdf5/cross_sections.xml'

# Define water and zircaloy materials (always at 600 K)
water = openmc.Material(name='H2O', temperature=600.0)
water.set_density(units='sum')
for nuc, density in water_comp[600]:
    water.add_nuclide(nuc, density)
water.add_s_alpha_beta('c_H_in_H2O')

zircaloy = openmc.Material(name='Zircaloy', temperature=600.0)
zircaloy.set_density('atom/b-cm', clad_density[600])
zircaloy.add_element('Zr', 1.0)

for T in 600, 900:
    # Create box to bound pin-cell -- dimensions depend on T
    x_min = openmc.XPlane(x0=-pitch[T]/2, boundary_type='reflective')
    x_max = openmc.XPlane(x0=+pitch[T]/2, boundary_type='reflective')
    y_min = openmc.YPlane(y0=-pitch[T]/2, boundary_type='reflective')
    y_max = openmc.YPlane(y0=+pitch[T]/2, boundary_type='reflective')
    z_min = openmc.ZPlane(z0=-10.0, boundary_type='reflective')
    z_max = openmc.ZPlane(z0=+10.0, boundary_type='reflective')
    box = +x_min & -x_max & +y_min & -y_max & +z_min & -z_max

    # Define source as box
    settings.source = openmc.Source(space=openmc.stats.Box(
        *box.bounding_box))

    # Surfaces for fuel/clad
    fuel_outer = openmc.ZCylinder(R=fuel_or[T])
    clad_inner = openmc.ZCylinder(R=clad_ir[T])
    clad_outer = openmc.ZCylinder(R=clad_or[T])

    # Define cells within pin-cell
    fuel = openmc.Cell(region=-fuel_outer)
    gap = openmc.Cell(region=+fuel_outer & -clad_inner)
    clad = openmc.Cell(fill=zircaloy, region=+clad_inner & -clad_outer)
    coolant = openmc.Cell(fill=water, region=+clad_inner)
    pincell = openmc.Universe(cells=(fuel, gap, clad, coolant))

    # Place pin-cell inside the box
    box_cell = openmc.Cell(fill=pincell, region=box)

    for model in ['uo2', 'reactor-mox', 'weapons-mox']:
        for enrich in enrichments[model]:
            # Create fuel material for given model/enrichment
            fuel_mat = openmc.Material(temperature=T)
            comp = composition[model]
            for nuc, density in zip(comp['nuclides'], comp['densities'][T][enrich]):
                fuel_mat.add_nuclide(nuc, density)
            fuel_mat.set_density(units='sum')

            # Assign fuel material to corresponding cell
            fuel.fill = fuel_mat

            # Create materials collection and overall geometry
            materials = openmc.Materials([water, zircaloy, fuel_mat])
            root_univ = openmc.Universe(0, cells=(box_cell,))
            geometry = openmc.Geometry(root_univ)

            # Create directory if it doesn't exist
            dirname = '{}-{}{}{}K'.format(model, enrich, os.path.sep, T)
            if not os.path.isdir(dirname):
                os.makedirs(dirname)

            # Export XML input files
            geometry.export_to_xml(os.path.join(dirname, 'geometry.xml'))
            materials.export_to_xml(os.path.join(dirname, 'materials.xml'))
            settings.export_to_xml(os.path.join(dirname, 'settings.xml'))
