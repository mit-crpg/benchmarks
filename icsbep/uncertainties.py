import csv

values = {}
with open('uncertainties.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for benchmark, case, mean, uncertainty in reader:
        if case:
            name = '{}/{}'.format(benchmark, case)
        else:
            name = benchmark
        values[name] = (float(mean), float(uncertainty))
