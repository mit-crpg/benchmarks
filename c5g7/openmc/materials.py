import openmc
import openmc.mgxs
import numpy as np

###############################################################################
#                 Exporting to OpenMC mg_cross_sections.xml File
###############################################################################

# Instantiate the energy group data
groups = openmc.mgxs.EnergyGroups(np.logspace(-11,1,8))

# Instantiate the 7-group C5G7 cross section data
uo2_xsdata = openmc.XSdata('uo2.300k', groups)
uo2_xsdata.order = 0
uo2_xsdata.total = np.array([1.779490E-01, 3.298050E-01, 4.803880E-01, 5.543670E-01, 3.118010E-01, 3.951680E-01, 5.644060E-01])
uo2_xsdata.absorption = np.array([8.02480E-03, 3.71740E-03, 2.67690E-02, 9.62360E-02, 3.00200E-02, 1.11260E-01, 2.82780E-01])
uo2_xsdata.scatter = np.array([[[1.275370E-01, 4.237800E-02, 9.437400E-06, 5.516300E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                [0.000000E-00, 3.244560E-01, 1.631400E-03, 3.142700E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                [0.000000E-00, 0.000000E-00, 4.509400E-01, 2.679200E-03, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                [0.000000E-00, 0.000000E-00, 0.000000E-00, 4.525650E-01, 5.566400E-03, 0.000000E-00, 0.000000E-00],
                                [0.000000E-00, 0.000000E-00, 0.000000E-00, 1.252500E-04, 2.714010E-01, 1.025500E-02, 1.002100E-08],
                                [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 1.296800E-03, 2.658020E-01, 1.680900E-02],
                                [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 8.545800E-03, 2.730800E-01]]])
uo2_xsdata.fission = np.array([7.212060E-03, 8.193010E-04, 6.453200E-03, 1.856480E-02, 1.780840E-02, 8.303480E-02, 2.160040E-01])
uo2_xsdata.nu_fission = np.array([2.005998E-02, 2.027303E-03, 1.570599E-02, 4.518301E-02, 4.334208E-02, 2.020901E-01, 5.257105E-01])
uo2_xsdata.chi = np.array([5.87910E-01, 4.11760E-01, 3.39060E-04, 1.17610E-07, 0.000000E-00, 0.000000E-00, 0.000000E-00])

mox43_xsdata = openmc.XSdata('mox43.300k', groups)
mox43_xsdata.order = 0
mox43_xsdata.total = np.array([1.787310E-01, 3.308490E-01, 4.837720E-01, 5.669220E-01, 4.262270E-01, 6.789970E-01, 6.828520E-01])
mox43_xsdata.absorption = np.array([8.43390E-03, 3.75770E-03, 2.79700E-02, 1.04210E-01, 1.39940E-01, 4.09180E-01, 4.09350E-01])
mox43_xsdata.scatter = np.array([[[1.288760E-01, 4.141300E-02, 8.229000E-06, 5.040500E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 3.254520E-01, 1.639500E-03, 1.598200E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 0.000000E-00, 4.531880E-01, 2.614200E-03, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 4.571730E-01, 5.539400E-03, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 1.604600E-04, 2.768140E-01, 9.312700E-03, 9.165600E-09],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 2.005100E-03, 2.529620E-01, 1.485000E-02],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 8.494800E-03, 2.650070E-01]]])
mox43_xsdata.fission = np.array([7.62704E-03, 8.76898E-04, 5.69835E-03, 2.28872E-02, 1.07635E-02, 2.32757E-01, 2.48968E-01])
mox43_xsdata.nu_fission = np.array([2.175300E-02, 2.535103E-03, 1.626799E-02, 6.547410E-02, 3.072409E-02, 6.666510E-01, 7.139904E-01])
mox43_xsdata.chi = np.array([5.87910E-01, 4.11760E-01, 3.39060E-04, 1.17610E-07, 0.000000E-00, 0.000000E-00, 0.000000E-00])

mox7_xsdata = openmc.XSdata('mox7.300k', groups)
mox7_xsdata.order = 0
mox7_xsdata.total = np.array([1.813230E-01, 3.343680E-01, 4.937850E-01, 5.912160E-01, 4.741980E-01, 8.336010E-01, 8.536030E-01])
mox7_xsdata.absorption = np.array([9.06570E-03, 4.29670E-03, 3.28810E-02, 1.22030E-01, 1.82980E-01, 5.68460E-01, 5.85210E-01])
mox7_xsdata.scatter = np.array([[[1.304570E-01, 4.179200E-02, 8.510500E-06, 5.132900E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                 [0.000000E-00, 3.284280E-01, 1.643600E-03, 2.201700E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                 [0.000000E-00, 0.000000E-00, 4.583710E-01, 2.533100E-03, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                 [0.000000E-00, 0.000000E-00, 0.000000E-00, 4.637090E-01, 5.476600E-03, 0.000000E-00, 0.000000E-00],
                                 [0.000000E-00, 0.000000E-00, 0.000000E-00, 1.761900E-04, 2.823130E-01, 8.728900E-03, 9.001600E-09],
                                 [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 2.276000E-03, 2.497510E-01, 1.311400E-02],
                                 [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 8.864500E-03, 2.595290E-01]]])
mox7_xsdata.fission = np.array([8.25446E-03, 1.32565E-03, 8.42156E-03, 3.28730E-02, 1.59636E-02, 3.23794E-01, 3.62803E-01])
mox7_xsdata.nu_fission = np.array([2.381395E-02, 3.858689E-03, 2.413400E-02, 9.436622E-02, 4.576988E-02, 9.281814E-01, 1.043200E+00])
mox7_xsdata.chi = np.array([5.87910E-01, 4.11760E-01, 3.39060E-04, 1.17610E-07, 0.000000E-00, 0.000000E-00, 0.000000E-00])

mox87_xsdata = openmc.XSdata('mox87.300k', groups)
mox87_xsdata.order = 0
mox87_xsdata.total = np.array([1.830450E-01, 3.367050E-01, 5.005070E-01, 6.061740E-01, 5.027540E-01, 9.210280E-01, 9.552310E-01])
mox87_xsdata.absorption = np.array([9.48620E-03, 4.65560E-03, 3.62400E-02, 1.32720E-01, 2.08400E-01, 6.58700E-01, 6.90170E-01])
mox87_xsdata.scatter = np.array([[[1.315040E-01, 4.204600E-02, 8.697200E-06, 5.193800E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 3.304030E-01, 1.646300E-03, 2.600600E-09, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 0.000000E-00, 4.617920E-01, 2.474900E-03, 0.000000E-00, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 4.680210E-01, 5.433000E-03, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 1.859700E-04, 2.857710E-01, 8.397300E-03, 8.928000E-09],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 2.391600E-03, 2.476140E-01, 1.232200E-02],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 8.968100E-03, 2.560930E-01]]])
mox87_xsdata.fission = np.array([8.67209E-03, 1.62426E-03, 1.02716E-02, 3.90447E-02, 1.92576E-02, 3.74888E-01, 4.30599E-01])
mox87_xsdata.nu_fission = np.array([2.518600E-02, 4.739509E-03, 2.947805E-02, 1.122500E-01, 5.530301E-02, 1.074999E+00, 1.239298E+00])
mox87_xsdata.chi = np.array([5.87910E-01, 4.11760E-01, 3.39060E-04, 1.17610E-07, 0.000000E-00, 0.000000E-00, 0.000000E-00])

fiss_chamber_xsdata = openmc.XSdata('fiss_chamber.300k', groups)
fiss_chamber_xsdata.order = 0
fiss_chamber_xsdata.total = np.array([1.260320E-01, 2.931600E-01, 2.842500E-01, 2.810200E-01, 3.344600E-01, 5.656400E-01, 1.172140E+00])
fiss_chamber_xsdata.absorption = np.array([5.11320E-04, 7.58130E-05, 3.16430E-04, 1.16750E-03, 3.39770E-03, 9.18860E-03, 2.32440E-02])
fiss_chamber_xsdata.scatter = np.array([[[6.616590E-02, 5.907000E-02, 2.833400E-04, 1.462200E-06, 2.064200E-08, 0.000000E-00, 0.000000E-00],
                                         [0.000000E-00, 2.403770E-01, 5.243500E-02, 2.499000E-04, 1.923900E-05, 2.987500E-06, 4.214000E-07],
                                         [0.000000E-00, 0.000000E-00, 1.834250E-01, 9.228800E-02, 6.936500E-03, 1.079000E-03, 2.054300E-04],
                                         [0.000000E-00, 0.000000E-00, 0.000000E-00, 7.907690E-02, 1.699900E-01, 2.586000E-02, 4.925600E-03],
                                         [0.000000E-00, 0.000000E-00, 0.000000E-00, 3.734000E-05, 9.975700E-02, 2.067900E-01, 2.447800E-02],
                                         [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 9.174200E-04, 3.167740E-01, 2.387600E-01],
                                         [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 4.979300E-02, 1.09910E+00]]])
fiss_chamber_xsdata.fission = np.array([4.79002E-09, 5.82564E-09, 4.63719E-07, 5.24406E-06, 1.45390E-07, 7.14972E-07, 2.08041E-06])
fiss_chamber_xsdata.nu_fission = np.array([1.323401E-08, 1.434500E-08, 1.128599E-06, 1.276299E-05, 3.538502E-07, 1.740099E-06, 5.063302E-06])
fiss_chamber_xsdata.chi = np.array([5.87910E-01, 4.11760E-01, 3.39060E-04, 1.17610E-07, 0.000000E-00, 0.000000E-00, 0.000000E-00])

guide_tube_xsdata = openmc.XSdata('guide_tube.300k', groups)
guide_tube_xsdata.order = 0
guide_tube_xsdata.total = np.array([1.260320E-01, 2.931600E-01, 2.842400E-01, 2.809600E-01, 3.344400E-01, 5.656400E-01, 1.172150E+00])
guide_tube_xsdata.absorption = np.array([5.11320E-04, 7.58010E-05, 3.15720E-04, 1.15820E-03, 3.39750E-03, 9.18780E-03, 2.32420E-02])
guide_tube_xsdata.scatter = np.array([[[6.616590E-02, 5.907000E-02, 2.833400E-04, 1.462200E-06, 2.064200E-08, 0.000000E-00, 0.000000E-00],
                                       [0.000000E-00, 2.403770E-01, 5.243500E-02, 2.499000E-04, 1.923900E-05, 2.987500E-06, 4.214000E-07],
                                       [0.000000E-00, 0.000000E-00, 1.832970E-01, 9.239700E-02, 6.944600E-03, 1.080300E-03, 2.056700E-04],
                                       [0.000000E-00, 0.000000E-00, 0.000000E-00, 7.885110E-02, 1.701400E-01, 2.588100E-02, 4.929700E-03],
                                       [0.000000E-00, 0.000000E-00, 0.000000E-00, 3.733300E-05, 9.973720E-02, 2.067900E-01, 2.447800E-02],
                                       [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 9.172600E-04, 3.167650E-01, 2.387700E-01],
                                       [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 4.979200E-02, 1.099120E+00]]])
guide_tube_xsdata.fission = np.zeros(7)
guide_tube_xsdata.nu_fission = np.zeros(7)
guide_tube_xsdata.chi = np.zeros(7)

water_xsdata = openmc.XSdata('water.300k', groups)
water_xsdata.order = 0
water_xsdata.total = np.array([1.592060E-01, 4.129700E-01, 5.903100E-01, 5.843500E-01, 7.180000E-01, 1.254450E+00, 2.650380E+00])
water_xsdata.absorption = np.array([6.01050E-04, 1.57930E-05, 3.37160E-04, 1.94060E-03, 5.74160E-03, 1.50010E-02, 3.72390E-02])
water_xsdata.scatter = np.array([[[4.447770E-02, 1.134000E-01, 7.234700E-04, 3.749900E-06, 5.318400E-08, 0.000000E-00, 0.000000E-00],
                                  [0.000000E-00, 2.823340E-01, 1.299400E-01, 6.234000E-04, 4.800200E-05, 7.448600E-06, 1.045500E-06],
                                  [0.000000E-00, 0.000000E-00, 3.452560E-01, 2.245700E-01, 1.699900E-02, 2.644300E-03, 5.034400E-04],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 9.102840E-02, 4.155100E-01, 6.373200E-02, 1.213900E-02],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 7.143700E-05, 1.391380E-01, 5.118200E-01, 6.122900E-02],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 2.215700E-03, 6.999130E-01, 5.373200E-01],
                                  [0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 0.000000E-00, 1.324400E-01, 2.480700E+00]]])
water_xsdata.fission = np.zeros(7)
water_xsdata.nu_fission = np.zeros(7)
water_xsdata.chi = np.zeros(7)

control_rod_xsdata = openmc.XSdata('control_rod.300k', groups)
control_rod_xsdata.order = 0
control_rod_xsdata.total = np.array([2.16768E-01, 4.80098E-01, 8.86369E-01, 9.70009E-01, 9.10482E-01, 1.13775E+00, 1.84048E+00])
control_rod_xsdata.absorption = np.array([1.70490E-03, 8.36224E-03, 8.37901E-02, 3.97797E-01, 6.98763E-01, 9.29508E-01, 1.17836E+00])
control_rod_xsdata.scatter = np.array([[[1.70563E-01, 4.44012E-02, 9.83670E-05, 1.27786E-07, 0.00000E-00, 0.00000E-00, 0.00000E-00],
                                        [0.00000E-00, 4.71050E-01, 6.85480E-04, 3.91395E-10, 0.00000E-00, 0.00000E-00, 0.00000E-00],
                                        [0.00000E-00, 0.00000E-00, 8.01859E-01, 7.20132E-04, 0.00000E-00, 0.00000E-00, 0.00000E-00],
                                        [0.00000E-00, 0.00000E-00, 0.00000E-00, 5.70752E-01, 1.46015E-03, 0.00000E-00, 0.00000E-00],
                                        [0.00000E-00, 0.00000E-00, 0.00000E-00, 6.55562E-05, 2.07838E-01, 3.81486E-03, 3.69760E-09],
                                        [0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00, 1.02427E-03, 2.02465E-01, 4.75290E-03],
                                        [0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00, 0.00000E-00, 3.53043E-03, 6.58597E-01]]])
control_rod_xsdata.fission = np.zeros(7)
control_rod_xsdata.nu_fission = np.zeros(7)
control_rod_xsdata.chi = np.zeros(7)

mg_cross_sections_file = openmc.MGXSLibraryFile(groups)
mg_cross_sections_file.add_xsdatas([uo2_xsdata, mox43_xsdata, mox7_xsdata, mox87_xsdata,
                                    fiss_chamber_xsdata, guide_tube_xsdata, water_xsdata,
                                    control_rod_xsdata])
mg_cross_sections_file.export_to_xml()


###############################################################################
#                 Exporting to OpenMC materials.xml File
###############################################################################

# Instantiate some Macroscopic Data
uo2_data = openmc.Macroscopic('uo2', '300k')
mox43_data = openmc.Macroscopic('mox43', '300k')
mox7_data = openmc.Macroscopic('mox7', '300k')
mox87_data = openmc.Macroscopic('mox87', '300k')
fiss_chamber_data = openmc.Macroscopic('fiss_chamber', '300k')
guide_tube_data = openmc.Macroscopic('guide_tube', '300k')
water_data = openmc.Macroscopic('water', '300k')
control_rod_data = openmc.Macroscopic('control_rod', '300k')

# Instantiate Materials dictionary
materials = {}

# Instantiate some Materials and register the appropriate Nuclides
materials['UO2'] = openmc.Material(material_id=1, name='UO2')
materials['UO2'].set_density('macro', 1.0)
materials['UO2'].add_macroscopic(uo2_data)

materials['MOX 4.3%'] = openmc.Material(material_id=2, name='MOX 4.3%')
materials['MOX 4.3%'].set_density('macro', 1.0)
materials['MOX 4.3%'].add_macroscopic(mox43_data)

materials['MOX 7.0%'] = openmc.Material(material_id=3, name='MOX 7.0%')
materials['MOX 7.0%'].set_density('macro', 1.0)
materials['MOX 7.0%'].add_macroscopic(mox7_data)

materials['MOX 8.7%'] = openmc.Material(material_id=4, name='MOX 8.7%')
materials['MOX 8.7%'].set_density('macro', 1.0)
materials['MOX 8.7%'].add_macroscopic(mox87_data)

materials['Fission Chamber'] = openmc.Material(material_id=5, name='Fission Chamber')
materials['Fission Chamber'].set_density('macro', 1.0)
materials['Fission Chamber'].add_macroscopic(fiss_chamber_data)

materials['Guide Tube'] = openmc.Material(material_id=6, name='Guide Tube')
materials['Guide Tube'].set_density('macro', 1.0)
materials['Guide Tube'].add_macroscopic(guide_tube_data)

materials['Water'] = openmc.Material(material_id=7, name='Water')
materials['Water'].set_density('macro', 1.0)
materials['Water'].add_macroscopic(water_data)

materials['Control Rod'] = openmc.Material(material_id=8, name='Control Rod')
materials['Control Rod'].set_density('macro', 1.0)
materials['Control Rod'].add_macroscopic(control_rod_data)
