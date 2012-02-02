#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math

# Read tally and uncertainty values
flux = []
unc = []
for line in open('tallies.out','r'):
    words = line.split()
    if words:
        if words[-2] == '+/-':
            flux.append(float(words[-3]))
            unc.append(2*float(words[-1]))

# Determine equal-lethargy width energies
n_bins = len(flux)
Emin = 1e-11
Emax = 20.0
u = math.log(Emax/Emin)/n_bins
E = [Emin*math.exp(i*u) for i in range(n_bins)]

# Make log-log plot with error bars
plt.errorbar(E,flux,yerr=unc, fmt='k.')
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.grid(which='both')
plt.xlabel('Energy (MeV)')
plt.ylabel('Flux')
plt.show()
