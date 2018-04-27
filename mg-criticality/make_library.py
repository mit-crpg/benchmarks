#!/usr/bin/env python

import numpy as np

import openmc

GROUP_STRUCT = {1: openmc.mgxs.EnergyGroups(group_edges=[0.0, 20.0e6]),
                2: openmc.mgxs.EnergyGroups(group_edges=[0.0, 0.625, 20.0e6]),
                3: openmc.mgxs.EnergyGroups(group_edges=[0.0, 0.625, 1.E3,
                                                         20.0e6]),
                6: openmc.mgxs.EnergyGroups(group_edges=[0.0, 0.625, 10., 1.E3,
                                                         1.e6, 10.e6, 20.0e6])}

###############################################################################
#                 Create OpenMC mgxs.h5 files
###############################################################################


def plot_it(scatter_matrix):
    import matplotlib.pyplot as plt
    import scipy.special as ss
    groups = scatter_matrix.shape[0]
    orders = scatter_matrix.shape[2]
    Nmu = 50
    mu = np.linspace(-1, 1, Nmu)
    f = np.zeros(shape=(groups, groups, Nmu))
    for gin in range(groups):
        for gout in range(groups):
            data = scatter_matrix[gin, gout, :]
            data /= data[0]
            for l in range(orders):
                f[gin, gout, :] += ((float(l) + 0.5) *
                                    ss.eval_legendre(l, mu) * data[l])

    i = 0
    for gin in range(groups):
        for gout in range(groups):
            i += 1
            plt.subplot(groups, groups, i)
            plt.title(str(gin + 1) + ' to ' + str(gout + 1))
            plt.plot(mu, f[gin, gout, :])
    plt.show()
    plt.close()


def set_it(name, groups, order, fission, nu, absorption, scatt, total, chi):
    xsd = openmc.XSdata(name, groups)
    xsd.order = order
    if fission is not None:
        xsd.set_fission(fission[:])
    if nu is not None and fission is not None:
        xsd.set_nu_fission(np.multiply(nu, fission))
    xsd.set_absorption(absorption[:])
    xsd.set_scatter_matrix(scatt[:, :, :])
    xsd.set_total(total[:])
    if chi is not None:
        xsd.set_chi(chi[:])
    return xsd


def create_1g():
    # Instantiate the energy group data and file object
    groups = GROUP_STRUCT[1]

    mg_cross_sections_file = openmc.MGXSLibrary(groups)

    ###########################################################################
    # PUa, Sec 4.1.1
    nu = 3.24
    fiss = [0.0816]
    capture = [0.019584]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.225216]]])
    total = [0.32640]
    chi = [1.]

    PUa = set_it('PUa', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(PUa)

    ###########################################################################
    # PUb, Sec 4.1.1
    nu = 2.84
    PUb = set_it('PUb', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(PUb)

    ###########################################################################
    # H2O, Sec 4.1.1
    nu = 0.
    fiss = None
    capture = [0.032640]
    absorption = capture
    scatter = np.array([[[0.293760]]])
    total = [0.32640]
    chi = None

    H2O = set_it('H2O', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(H2O)

    ###########################################################################
    # Ua, Sec 4.1.2
    nu = 2.70
    fiss = [0.065280]
    capture = [0.013056]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.248064]]])
    total = [0.32640]
    chi = [1.]

    Ua = set_it('Ua', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Ua)

    ###########################################################################
    # Ub, Sec 4.1.2
    nu = 2.797101
    Ub = set_it('Ub', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Ub)

    ###########################################################################
    # Uc, Sec 4.1.2
    nu = 2.707308
    Uc = set_it('Uc', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Uc)

    ###########################################################################
    # Ud, Sec 4.1.2
    nu = 2.679198
    Ud = set_it('Ud', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Ud)

    ###########################################################################
    # UD2O, Sec 4.1.3
    nu = 1.70
    fiss = [0.054628]
    capture = [0.027314]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.464338]]])
    total = [0.54628]
    chi = [1.]

    UD2O = set_it('UD2O', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(UD2O)

    ###########################################################################
    # H2O, Sec 4.1.3
    nu = 0.
    fiss = None
    capture = [0.054628]
    absorption = capture
    scatter = np.array([[[0.491652]]])
    total = [0.54628]
    chi = None

    H2O_2 = set_it('H2O_2', groups, 0, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(H2O_2)

    ###########################################################################
    # Ue, Sec 4.1.4
    nu = 2.50
    fiss = [0.06922744]
    capture = [0.01013756]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.328042]]])
    total = [0.407407]
    chi = [1.]

    Ue = set_it('Ue', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Ue)

    ###########################################################################
    # Fe, Sec 4.1.4
    nu = 0.
    fiss = None
    capture = [0.00046512]
    absorption = capture
    scatter = np.array([[[0.23209488]]])
    total = [0.23256]
    chi = None

    Fe = set_it('Fe', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Fe)

    ###########################################################################
    # Na, Sec 4.1.4
    nu = 0.
    fiss = None
    capture = [0.0]
    absorption = capture
    scatter = np.array([[[0.086368032]]])
    total = [0.086368032]
    chi = None

    Na = set_it('Na', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Na)

    ###########################################################################
    # PUa-1, Sec 4.1.4
    nu = 2.5
    fiss = [0.266667]
    capture = [0.0]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.733333, 0.2]]])
    total = [1.]
    chi = [1.]

    PUa_1 = set_it('PUa1', groups, 1, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(PUa_1)

    ###########################################################################
    # PUb-2, Sec 4.2.1
    scatter = np.array([[[0.733333, 0.333333]]])
    PUb_1 = set_it('PUb1', groups, 1, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(PUb_1)

    ###########################################################################
    # PUa-2, Sec 4.1.4
    nu = 2.5
    fiss = [0.266667]
    capture = [0.0]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.733333, 0.2, 0.075]]])
    total = [1.]
    chi = [1.]

    PUa_2 = set_it('PUa2', groups, 2, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(PUa_2)

    ###########################################################################
    # PUb-2, Sec 4.2.1
    scatter = np.array([[[0.733333, 0.333333, 0.125]]])
    PUb_2 = set_it('PUb2', groups, 2, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(PUb_2)

    ###########################################################################
    # Ua-1, Sec 4.1.4
    nu = 2.70
    fiss = [0.065280]
    capture = [0.013056]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.248064, 0.042432]]])
    total = [0.32640]
    chi = [1.]

    Ua_1 = set_it('Ua1', groups, 1, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Ua_1)

    ###########################################################################
    # Ub-1, Sec 4.2.1
    scatter = np.array([[[0.248064, 0.212160]]])
    Ub_1 = set_it('Ub1', groups, 1, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Ub_1)

    ###########################################################################
    # UD2Oa-1, Sec 4.2.3
    nu = 1.808381
    fiss = [0.054628]
    capture = [0.027314]
    absorption = np.add(capture, fiss)
    scatter = np.array([[[0.464338, 0.056312624]]])
    total = [0.54628]
    chi = [1.]

    UD2Oa = set_it('UD2Oa', groups, 1, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(UD2Oa)

    ###########################################################################
    # UD2Ob-1, Sec 4.2.3
    nu = 1.841086
    scatter = np.array([[[0.464338, 0.112982569]]])
    UD2Ob = set_it('UD2Ob', groups, 1, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(UD2Ob)

    ###########################################################################
    # UD2Oc-1, Sec 4.2.3
    nu = 1.6964
    scatter = np.array([[[0.464338, -0.27850447]]])
    UD2Oc = set_it('UD2Oc', groups, 1, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(UD2Oc)

    mg_cross_sections_file.export_to_hdf5('1g.h5')


def create_2g():
    # Instantiate the energy group data and file object
    groups = GROUP_STRUCT[2]

    mg_cross_sections_file = openmc.MGXSLibrary(groups)

    ###########################################################################
    # 5.1.1 Pu
    nu = [3.10, 2.93]
    fiss = np.array([0.0936, 0.08544])
    capture = [0.00480, 0.0144]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.0792, 0.0432],
          [0.00000, 0.23616]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.2208, 0.3360]
    chi = [0.575, 0.425]

    Pu = set_it('Pu', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(Pu)

    ###########################################################################
    # 5.1.2 U
    nu = [2.70, 2.5]
    fiss = np.array([0.06192, 0.06912])
    capture = [0.00384, 0.01344]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.078240, 0.0720],
          [0.00000, 0.26304]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.2160, 0.3456]
    chi = [0.575, 0.425]

    U = set_it('U', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(U)

    ###########################################################################
    # 5.1.3 UAl
    nu = [0.0, 2.830023]
    fiss = np.array([0.0, 0.060706])
    capture = [0.000217, 0.003143]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.247516, 0.020432],
          [0.000000, 1.213127]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.268165, 1.276976]
    chi = [1.0, 0.0]

    UAl = set_it('UAl', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(UAl)

    ###########################################################################
    # 5.1.4 URRa-0
    nu = [2.5, 2.5]
    fiss = np.array([0.0010484, 0.050632])
    capture = [0.0010046, 0.025788]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.62568, 0.029227],
          [0.00000, 2.443830]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.65696, 2.52025]
    chi = [1., 0.]

    URRa_0 = set_it('URRa0', groups, 0, fiss, nu, absorption, scatter, total,
                    chi)
    mg_cross_sections_file.add_xsdata(URRa_0)

    ###########################################################################
    # 5.1.4 URRb-0
    fiss = np.array([0.000836, 0.029564])
    capture = [0.001104, 0.024069]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.838920, 0.046350],
          [0.000767, 2.918300]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.88721, 2.9727]
    chi = [1., 0.]

    URRb_0 = set_it('URRb0', groups, 0, fiss, nu, absorption, scatter, total,
                    chi)
    mg_cross_sections_file.add_xsdata(URRb_0)

    ###########################################################################
    # 5.1.4 URRc-0
    fiss = np.array([0.001648, 0.057296])
    capture = [0.001472, 0.029244]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.838070, 0.045360],
          [0.001160, 2.8751]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.88655, 2.9628]
    chi = [1., 0.]

    URRc_0 = set_it('URRc0', groups, 0, fiss, nu, absorption, scatter, total,
                    chi)
    mg_cross_sections_file.add_xsdata(URRc_0)

    ###########################################################################
    # 5.1.4 H2Oa
    nu = None
    fiss = None
    capture = [0.00074, 0.018564]
    absorption = capture
    scatter = np.array(
        [[[0.839750, 0.04749],
          [0.000336, 2.96760]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.88798, 2.9865]
    chi = None

    H2Oa = set_it('H2Oa', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(H2Oa)

    ###########################################################################
    # 5.1.4 URRd-0
    nu = [1.004, 2.50]
    fiss = np.array([0.61475, 0.045704])
    capture = [0.0019662, 0.023496]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.000000, 0.0342008],
          [0.000000, 2.0688000]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.650917, 2.13800]
    chi = [1., 0.]

    URRd_0 = set_it('URRd0', groups, 0, fiss, nu, absorption, scatter, total,
                    chi)
    mg_cross_sections_file.add_xsdata(URRd_0)

    ###########################################################################
    # 5.1.4 H2Ob
    nu = None
    fiss = None
    capture = [8.480293E-6, 0.00016]
    absorption = capture
    scatter = np.array(
        [[[0.1096742149, 0.001000595707],
          [0.0000000000, 0.363390000000]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.1106832906, 0.36355]
    chi = None

    H2Ob = set_it('H2Ob', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(H2Ob)

    ###########################################################################
    # 5.1.4 H2Oc
    nu = None
    fiss = None
    capture = [4.97229E-4, 0.0188]
    absorption = capture
    scatter = np.array(
        [[[1.226381244, 0.1046395340],
          [0.0000000000, 4.35470]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [1.331518007, 4.37350]
    chi = None

    H2Oc = set_it('H2Oc', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(H2Oc)

    ###########################################################################
    # 5.1.5 UD2O
    nu = [2.50, 2.50]
    fiss = np.array([0.002817, 0.097])
    capture = [0.0087078, 0.02518]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.31980, 0.0045552],
          [0.000000, 0.42410]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.33588, 0.54628]
    chi = [1., 0.]

    UD2O = set_it('UD2O', groups, 0, fiss, nu, absorption, scatter, total,
                  chi)
    mg_cross_sections_file.add_xsdata(UD2O)

    ###########################################################################
    # 5.2.1 URR-1
    nu = [2.5, 2.5]
    fiss = np.array([0.0010484, 0.050632])
    capture = [0.0010046, 0.025788]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.62568, 0.27459], [0.029227, 0.0075737]],
         [[0.00000, 0.00000], [2.443830, 0.8331800]]])
    total = [0.65696, 2.52025]
    chi = [1., 0.]

    URR_1 = set_it('URR1', groups, 1, fiss, nu, absorption, scatter, total,
                   chi)
    mg_cross_sections_file.add_xsdata(URR_1)

    ###########################################################################
    # 5.2.2 UD2O-1
    nu = [2.50, 2.50]
    fiss = np.array([0.0028172, 0.097])
    capture = [0.0087078, 0.02518]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.31980, 0.06694], [0.004555, -0.0003972]],
         [[0.00000, 0.00000], [0.424100, 0.05439000]]])
    total = [0.33588, 0.54628]
    chi = [1., 0.]

    UD2O_1 = set_it('UD2O1', groups, 1, fiss, nu, absorption, scatter, total,
                    chi)
    mg_cross_sections_file.add_xsdata(UD2O_1)

    # Write the file
    mg_cross_sections_file.export_to_hdf5('2g.h5')


def create_3g():
    # Instantiate the energy group data and file object
    groups = GROUP_STRUCT[3]

    mg_cross_sections_file = openmc.MGXSLibrary(groups)

    ###########################################################################
    # 6 URR
    nu = [3.0, 2.5, 2.0]
    fiss = np.array([0.006, 0.060, 0.90])
    capture = [0.006, 0.040, 0.20]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.024, 0.171, 0.033],
          [0.000, 0.600, 0.275],
          [0.000, 0.000, 2.000]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.240, 0.975, 3.10]
    chi = [0.96, 0.05, 0.0]

    URR = set_it('URR', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(URR)

    mg_cross_sections_file.export_to_hdf5('3g.h5')


def create_6g():
    # Instantiate the energy group data and file object
    groups = GROUP_STRUCT[6]

    mg_cross_sections_file = openmc.MGXSLibrary(groups)

    ###########################################################################
    # 7 URR
    nu = [3.0, 2.5, 2.0, 2.0, 2.50, 3.0]
    fiss = np.array([0.006, 0.060, 0.90, 0.90, 0.060, 0.006])
    capture = [0.006, 0.040, 0.20, 0.2, 0.04, 0.006]
    absorption = np.add(capture, fiss)
    scatter = np.array(
        [[[0.024, 0.171, 0.033, 0.00, 0.00, 0.00],
          [0.000, 0.600, 0.275, 0.00, 0.00, 0.00],
          [0.000, 0.000, 2.000, 0.00, 0.00, 0.00],
          [0.000, 0.000, 0.000, 2.00, 0.00, 0.00],
          [0.000, 0.000, 0.000, 0.275, 0.60, 0.00],
          [0.000, 0.000, 0.000, 0.033, 0.171, 0.024]]])
    scatter = np.rollaxis(scatter, 0, 3)
    total = [0.240, 0.975, 3.10, 3.10, 0.975, 0.240]
    chi = [0.48, 0.02, 0.0, 0.0, 0.02, 0.48]

    URR = set_it('URR', groups, 0, fiss, nu, absorption, scatter, total, chi)
    mg_cross_sections_file.add_xsdata(URR)

    mg_cross_sections_file.export_to_hdf5('6g.h5')


def create_specific_library(groups):
    if groups == 1:
        create_1g()
    elif groups == 2:
        create_2g()
    elif groups == 3:
        create_3g()
    elif groups == 6:
        create_6g()


def create_all():
    for groups in [1, 2, 3, 6]:
        create_specific_library(groups)


if __name__ == "__main__":
    create_1g()
    create_2g()
    create_3g()
    create_6g()
