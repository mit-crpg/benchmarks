#!/usr/bin/env python

from optparse import OptionParser
import csv

import repo
import make_library


def print_case(case):
    bias = 1.0E5 * (case.keff - case.ref_k)
    print('\tCalculated keff = {0:1.6f}'.format(case.keff))
    print('\tReference keff  = {0:1.6f}'.format(case.ref_k))
    print('\tBias [pcm]      = {0:1.1f}'.format(bias))
    return bias


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
case_nums = []
case_names = []
biases = []
codes = []
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
            bias = 0.
        else:
            bias = print_case(case)
        biases.append(bias)
        case_names.append(case.name)
        case_nums.append(case_num)

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
        bias = print_case(case)

        biases.append(bias)
        case_names.append(case.name)
        codes.append(code)
        case_nums.append(case.number)


# Write to a CSV
with open("results.csv", mode="w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",", quotechar='"',
                        quoting=csv.QUOTE_NONNUMERIC)

    # write the header
    writer.writerow(['Case ID', 'Case Name', 'Eigenvalue Bias [pcm]',
                     'Eigenvalue Bias Std. Dev. [pcm]', 'Error Code'])

    # Now run each case
    for i in range(len(case_nums)):
        writer.writerow([case_nums[i], case_names[i], biases[i].n,
                         biases[i].s, codes[i]])
