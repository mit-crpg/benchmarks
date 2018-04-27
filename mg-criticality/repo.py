#!/usr/bin/env python

from make_model import Case

# GLOBAL DATA
batches = 600
inactive = 100
particles = 100000
tab_leg = {'enable': True, 'num_points': 33}
# tab_leg = {'enable': False, 'num_points': 33}


def build_cases():

    cases = []
    names = {}

    # CASE 1
    case = 1
    name = 'PUa-1-0-IN'
    mat_names = ['PUa']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [9.4959]
    ref_k = 2.612903
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 2
    case = 2
    name = 'PUa-1-0-SL'
    mat_names = ['PUa']
    groups = 1
    order = 0
    geom = 'SL'
    rad = [1.853722]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 3
    case = 3
    name = 'PUa-H2O(1)-1-0-SL'
    mat_names = ['PUa', 'H2O']
    groups = 1
    order = 0
    geom = 'SL-NS'
    rad = [1.478450, 4.542175]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 4
    case = 4
    name = 'PUa-H2O(0.5)-1-0-SL'
    mat_names = ['PUa', 'H2O']
    groups = 1
    order = 0
    geom = 'SL'
    rad = [1.317862, 2.849725]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 5
    case = 5
    name = 'PUb-1-0-IN'
    mat_names = ['PUb']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [9.4959]
    ref_k = 2.290323
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 6
    case = 6
    name = 'PUb-1-0-SL'
    mat_names = ['PUb']
    groups = 1
    order = 0
    geom = 'SL'
    rad = [2.256751]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 7
    case = 7
    name = 'PUb-1-0-CY'
    mat_names = ['PUb']
    groups = 1
    order = 0
    geom = 'CY'
    rad = [4.279960]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 8
    case = 8
    name = 'PUb-1-0-SP'
    mat_names = ['PUb']
    groups = 1
    order = 0
    geom = 'SP'
    rad = [6.082547]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 9
    case = 9
    name = 'PUb-H2O(1)-1-0-CY'
    mat_names = ['PUb', 'H2O']
    groups = 1
    order = 0
    geom = 'CY'
    rad = [3.397610, 6.461335]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 10
    case = 10
    name = 'PUb-H2O(10)-1-0-CY'
    mat_names = ['PUb', 'H2O']
    groups = 1
    order = 0
    geom = 'CY'
    rad = [3.077574, 33.714829]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 11
    case = 11
    name = 'Ua-1-0-IN'
    mat_names = ['Ua']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.25
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 12
    case = 12
    name = 'Ua-1-0-SL'
    mat_names = ['Ua']
    groups = 1
    order = 0
    geom = 'SL'
    rad = [2.872934]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 13
    case = 13
    name = 'Ua-1-0-CY'
    mat_names = ['Ua']
    groups = 1
    order = 0
    geom = 'CY'
    rad = [5.284935]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 14
    case = 14
    name = 'Ua-1-0-SP'
    mat_names = ['Ua']
    groups = 1
    order = 0
    geom = 'SP'
    rad = [7.428998]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 15
    case = 15
    name = 'Ub-1-0-IN'
    mat_names = ['Ub']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.330917
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 16
    case = 16
    name = 'Ub-H2O(1)-1-0-SP'
    mat_names = ['Ub', 'H2O']
    groups = 1
    order = 0
    geom = 'SP'
    rad = [6.12745, 9.191176]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 17
    case = 17
    name = 'Uc-1-0-IN'
    mat_names = ['Uc']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.256083
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 18
    case = 18
    name = 'Uc-H2O(2)-1-0-SP'
    mat_names = ['Uc', 'H2O']
    groups = 1
    order = 0
    geom = 'SP'
    rad = [6.12745, 12.2549]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 19
    case = 19
    name = 'Ud-1-0-IN'
    mat_names = ['Ud']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.232667
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 20
    case = 20
    name = 'Ud-H2O(1)-1-0-SP'
    mat_names = ['Ud', 'H2O']
    groups = 1
    order = 0
    geom = 'SP'
    rad = [6.12745, 15.318626]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 21
    case = 21
    name = 'UD2O-1-0-IN'
    mat_names = ['UD2O']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 1.133333
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 22
    case = 22
    name = 'UD2O-1-0-SL'
    mat_names = ['UD2O']
    groups = 1
    order = 0
    geom = 'SL'
    rad = [10.371065]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 23
    case = 23
    name = 'UD2O-1-0-CY'
    mat_names = ['UD2O']
    groups = 1
    order = 0
    geom = 'CY'
    rad = [16.554249]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 24
    case = 24
    name = 'UD2O-1-0-SP'
    mat_names = ['UD2O']
    groups = 1
    order = 0
    geom = 'SP'
    rad = [22.017156]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 25
    case = 25
    name = 'UD2O-H2O(1)-1-0-SL'
    mat_names = ['UD2O', 'H2O_2']
    groups = 1
    order = 0
    geom = 'SL'
    rad = [9.214139, 11.044702]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 26
    case = 26
    name = 'UD2O-H2O(10)-1-0-SL'
    mat_names = ['UD2O', 'H2O_2']
    groups = 1
    order = 0
    geom = 'SL'
    rad = [8.428096, 26.733726]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 27
    case = 27
    name = 'UD2O-H2O(1)-1-0-CY'
    mat_names = ['UD2O', 'H2O_2']
    groups = 1
    order = 0
    geom = 'CY'
    rad = [15.396916, 17.227479]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 28
    case = 28
    name = 'UD2O-H2O(10)-1-0-CY'
    mat_names = ['UD2O', 'H2O_2']
    groups = 1
    order = 0
    geom = 'CY'
    rad = [14.606658, 32.912288]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 29
    case = 29
    name = 'Ue-1-0-IN'
    mat_names = ['Ue']
    groups = 1
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.1806667
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 30
    case = 30
    name = 'Ue-Fe-Na-1-0-SL'
    mat_names = ['Fe', 'Ue', 'Fe', 'Na']
    groups = 1
    order = 0
    geom = 'FENA'
    rad = [0.317337461, 5.437057544, 5.754395005, 7.757166007]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 31
    case = 31
    name = 'PU-1-1-IN'
    mat_names = ['PUa2']
    groups = 1
    order = 1
    geom = 'IN'
    rad = [1.]
    ref_k = 2.5
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 32
    case = 32
    name = 'PUa-1-1-SL'
    mat_names = ['PUa2']
    groups = 1
    order = 1
    geom = 'SL'
    rad = [0.77032]
    ref_k = 1.
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 33
    case = 33
    name = 'PUa-1-2-SL'
    mat_names = ['PUa2']
    groups = 1
    order = 2
    geom = 'SL'
    rad = [0.76378]
    ref_k = 1.
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 34
    case = 34
    name = 'PUb-1-1-SL'
    mat_names = ['PUb2']
    groups = 1
    order = 1
    geom = 'SL'
    rad = [0.79606]
    ref_k = 1.
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 35
    case = 35
    name = 'PUb-1-2-SL'
    mat_names = ['PUb2']
    groups = 1
    order = 2
    geom = 'SL'
    rad = [0.78396]
    ref_k = 1.
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # # CASE -11
    # case = -11
    # name = 'Ua-1-1-IN'
    # mat_names = ['Ua1']
    # groups = 1
    # order = 1
    # geom = 'IN'
    # rad = [1.]
    # ref_k = 2.25
    # mesh_dim = [20, 1, 1]
    # params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
    #           'inactive': inactive, 'particles': particles}
    # cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
    #                   params))
    # names[name] = len(cases) - 1

    # CASE 36
    case = 36
    name = 'Ua-1-1-CY'
    mat_names = ['Ua1']
    groups = 1
    order = 1
    geom = 'CY'
    rad = [5.514296811]
    ref_k = 1.
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 37
    case = 37
    name = 'Ub-1-1-CY'
    mat_names = ['Ub1']
    groups = 1
    order = 1
    geom = 'CY'
    rad = [6.940205668]
    ref_k = 1.
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 38
    case = 38
    name = 'UD2Oa-1-1-IN'
    mat_names = ['UD2Oa']
    groups = 1
    order = 1
    geom = 'IN'
    rad = [1.]
    ref_k = 1.205587
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 39
    case = 39
    name = 'UD2Oa-1-1-SP'
    mat_names = ['UD2Oa']
    groups = 1
    order = 1
    geom = 'SP'
    rad = [18.30563081]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 40
    case = 40
    name = 'UD2Ob-1-1-IN'
    mat_names = ['UD2Ob']
    groups = 1
    order = 1
    geom = 'IN'
    rad = [1.]
    ref_k = 1.227391
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 41
    case = 41
    name = 'UD2Ob-1-1-SP'
    mat_names = ['UD2Ob']
    groups = 1
    order = 1
    geom = 'SP'
    rad = [18.30563081]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 42
    case = 42
    name = 'UD2Oc-1-1-IN'
    mat_names = ['UD2Oc']
    groups = 1
    order = 1
    geom = 'IN'
    rad = [1.]
    ref_k = 1.130933
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 43
    case = 43
    name = 'UD2Oc-1-1-SP'
    mat_names = ['UD2Oc']
    groups = 1
    order = 1
    geom = 'SP'
    rad = [18.30563081]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 44
    case = 44
    name = 'PU-2-0-IN'
    mat_names = ['Pu']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.683767
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 45
    case = 45
    name = 'PU-2-0-SL'
    mat_names = ['Pu']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [1.795602]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 46
    case = 46
    name = 'PU-2-0-SP'
    mat_names = ['Pu']
    groups = 2
    order = 0
    geom = 'SP'
    rad = [5.231567]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 47
    case = 47
    name = 'U-2-0-IN'
    mat_names = ['U']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.216349
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 48
    case = 48
    name = 'U-2-0-SL'
    mat_names = ['U']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [3.006375]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 49
    case = 49
    name = 'U-2-0-SP'
    mat_names = ['U']
    groups = 2
    order = 0
    geom = 'SP'
    rad = [7.909444]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 50
    case = 50
    name = 'UAL-2-0-IN'
    mat_names = ['UAl']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 2.662437
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 51
    case = 51
    name = 'UAL-2-0-SL'
    mat_names = ['UAl']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [7.830776]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 52
    case = 52
    name = 'UAL-2-0-SP'
    mat_names = ['UAl']
    groups = 2
    order = 0
    geom = 'SP'
    rad = [17.66770]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 53
    case = 53
    name = 'URRa-2-0-IN'
    mat_names = ['URRa0']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 1.631452
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 54
    case = 54
    name = 'URRa-2-0-SL'
    mat_names = ['URRa0']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [7.566853]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 55
    case = 55
    name = 'URRa-2-0-SP'
    mat_names = ['URRa0']
    groups = 2
    order = 0
    geom = 'SP'
    rad = [16.049836]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 56
    case = 56
    name = 'URRb-2-0-IN'
    mat_names = ['URRb0']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 1.365821
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 57
    case = 57
    name = 'URRc-2-0-IN'
    mat_names = ['URRc0']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 1.633380
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 58
    case = 58
    name = 'URRb-H2Oa(1)-2-0-SL'
    mat_names = ['URRb0', 'H2Oa']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [6.696802, 7.822954]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 59
    case = 59
    name = 'URRb-H2Oa(5)-2-0-SL'
    mat_names = ['URRb0', 'H2Oa']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [4.863392, 10.494149]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 60
    case = 60
    name = 'URRb-H2Oa(IN)-2-0-SL'
    mat_names = ['URRb0', 'H2Oa']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [4.686230, 1.e50]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 61
    case = 61
    name = 'URRc-H2Oa(IN)-2-0-SL'
    mat_names = ['URRc0', 'H2Oa']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [2.461903, 1.e50]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 62
    case = 62
    name = 'URRd-2-0-IN'
    mat_names = ['URRd0']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 1.034970
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 63
    case = 63
    name = 'URRd-H2Ob(1)-2-0-ISLC'
    mat_names = ['URRd0', 'H2Ob']
    groups = 2
    order = 0
    geom = 'ISLC'
    rad = [0.0329074, 9.067695]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 64
    case = 64
    name = 'URRd-H2Ob(10)-2-0-ISLC'
    mat_names = ['URRd0', 'H2Ob']
    groups = 2
    order = 0
    geom = 'ISLC'
    rad = [0.460135, 90.808010]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 65
    case = 65
    name = 'URRd-H2Oc(1)-2-0-ISLC'
    mat_names = ['URRd0', 'H2Oc']
    groups = 2
    order = 0
    geom = 'ISLC'
    rad = [0.341011, 1.092034]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 66
    case = 66
    name = 'URRd-H2Oc(10)-2-0-ISLC'
    mat_names = ['URRd0', 'H2Oc']
    groups = 2
    order = 0
    geom = 'ISLC'
    rad = [2.719087, 10.229312]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 67
    case = 67
    name = 'UD2O-2-0-IN'
    mat_names = ['UD2O']
    groups = 2
    order = 0
    geom = 'IN'
    rad = [1.]
    ref_k = 1.000221
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 68
    case = 68
    name = 'UD2O-2-0-SL'
    mat_names = ['UD2O']
    groups = 2
    order = 0
    geom = 'SL'
    rad = [846.632726]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 69
    case = 69
    name = 'UD2O-2-0-SP'
    mat_names = ['UD2O']
    groups = 2
    order = 0
    geom = 'SP'
    rad = [1695.337621]
    ref_k = 1.0
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 70

    ###################### SOMETHING WRONG WITH LIBRARY< MAT_NAMES SHOULD BE URR1
    case = 70
    name = 'URRa-2-1-IN'
    mat_names = ['URR1']
    groups = 2
    order = 1
    geom = 'IN'
    rad = [9.4959]
    ref_k = 1.631452
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 71
    case = 71
    name = 'URRa-2-1-SL'
    mat_names = ['URR1']
    geom = 'SL'
    ref_k = 1.0
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 72
    case = 72
    name = 'UD2O-2-1-IN'
    mat_names = ['UD2O1']
    groups = 2
    order = 1
    geom = 'IN'
    rad = [929.45]
    ref_k = 1.000227
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 73
    case = 73
    name = 'UD2O-2-1-SL'
    geom = 'SL'
    ref_k = 1.0
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 74
    case = 74
    name = 'URR-3-0-IN'
    mat_names = ['URR']
    groups = 3
    order = 1
    geom = 'IN'
    rad = [929.45]
    ref_k = 1.6
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    # CASE 75
    name = 'URR-6-0-IN'
    mat_names = ['URR']
    groups = 6
    order = 1
    geom = 'IN'
    rad = [929.45]
    ref_k = 1.6
    mesh_dim = [20, 1, 1]
    params = {'mesh_dim': mesh_dim, 'tab_leg': tab_leg, 'batches': batches,
              'inactive': inactive, 'particles': particles}
    cases.append(Case(case, name, mat_names, groups, order, geom, rad, ref_k,
                      params))
    names[name] = len(cases) - 1

    return cases, names

cases, names = build_cases()
