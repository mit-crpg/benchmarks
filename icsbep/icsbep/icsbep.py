import csv
import os

cwd = os.path.dirname(os.path.realpath(__file__))

model_keff = {}
with open(os.path.join(cwd, 'uncertainties.csv'), 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for benchmark, case, mean, uncertainty in reader:
        if case:
            name = '{}/{}'.format(benchmark, case)
        else:
            name = benchmark
        model_keff[name] = (float(mean), float(uncertainty))
