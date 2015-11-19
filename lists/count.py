#!/usr/bin/env python

import sys
from collections import defaultdict
from tabulate import tabulate

count = defaultdict(int)
for line in open(sys.argv[1]):
    words = line.split('/')
    model = words[1].split('-')
    cat = model[0][0] + model[2][0]
    if cat not in count:
        count[cat] = 0
    count[cat] += 1

headers = ["Fuel", "therm", "inter", "fast", "mixed"]
table = [['HEU', count['ht'], count['hi'], count['hf'], count['hm']],
         ['LEU', count['lt'], count['li'], count['lf'], count['lm']],
         ['IEU', count['it'], count['ii'], count['if'], count['im']],
         ['Pu', count['pt'], count['pi'], count['pf'], count['pm']],
         ['U233', count['ut'], count['ui'], count['uf'], count['um']],
         ['Mix', count['mt'], count['mi'], count['mf'], count['mm']]]
print(tabulate(table, headers=headers, tablefmt="grid"))
