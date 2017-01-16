#!/usr/bin/env python

from __future__ import print_function
from optparse import OptionParser

import matplotlib.pyplot as plt
import numpy as np

import repo
import make_library


def print_case(case):
    bias = np.abs(1.0E5 * (case.keff[0] - case.ref_k))
    print('\tCalculated keff = {0:1.6f}'.format(case.keff[0]))
    print('\tReference keff  = {0:1.6f}'.format(case.ref_k))
    print('\tBias [pcm]      = {0:1.1f}'.format(bias))


# Command line parsing
parser = OptionParser()
parser.add_option('-r', '--case', dest='case_name', default=None,
                  help="Run specific case instead of all cases.")
parser.add_option('-l', '--list', action="store_true",
                  dest="list_cases", default=False,
                  help="List out all benchmark cases.")
(options, args) = parser.parse_args()

# Check to see if we should just print case information to user
if options.list_cases:
    for key in repo.names:
        print('Case Name: {0}'.format(key))
    exit()

# Run specific case, if requested
if options.case_name:
    if options.case_name in repo.names:
        case_num = repo.names[options.case_name]
        case = repo.cases[case_num]

        print('Writing MGXS Library\n')
        make_library.create_specific_library(case.groups)

        print('Running Case\n')
        case.make_model()
        code = case.execute(False)
        if code != 0:
            print(case.name + ' Failed Execution!')
        else:
            print_case(case)

    else:
        print('Invalid Case Name: ' + options.case)

else:
    # Run them all
    print('Writing MGXS Libraries\n')
    make_library.create_all()

    print('Running Cases\n')
    for case in repo.cases:
        print(case.number, case.name)
        case.make_model()
        code = case.execute(True)
        if code != 0:
            print(case.name + ' Failed Execution!')
        else:
            print_case(case)
