================================
Reactor Physics Benchmark Models
================================

This repository contains a collection of benchmark models for the OpenMC and
other Monte Carlo particle transport codes. The following benchmark models are
currently available:

doppler-defect
  Benchmark for Doppler reactivity defect by Russell Mosteller. Described in
  LA-UR-06-2968_.

icsbep 
  Problems from the `International Handbook of Evaluated Criticality Safety
  Benchmark Experiments`_.

indc-usa-107
  Simple pin-cell model to test S(a,b) treatment in Monte Carlo codes. See
  `INDC(USA)-107`_.

mc-performance
  The `Monte Carlo Performance Benchmark`_ originally proposed by J. Eduard
  Hoogenboom and William Martin.

opr
  A BOL model of a Optimized Power Reactor 1000 (OPR1000) from South Korea. See
  Lee M.J. et al., "Monte Carlo Reactor Calculation with Substantially Reduced
  Number of Cycles", *Proceedings of PHYSOR 2012*, Knoxville, TN (2012).

source-convergence
  The `OECD/NEA Source Convergence Benchmarks`_ which include a checkerboard
  storage of assemblies, a pincell array with irradiated fuel, three thick
  one-dimensional slabs, and an array of interacting spheres.

c5g7
  The OECD/NEA C5G7_ Benchmarks which include multi-group benchmarks typically
  for deterministic transport problems.  This set includes a pincell, the
  2D 2x2 UO2 and MOX assembly array, and a 3D version of the 2x2 UO2 and MOX
  assembly array.

.. _LA-UR-06-2968: http://mcd.ans.org/jb/bench/Doppler/Overview.pdf

.. _International Handbook of Evaluated Criticality Safety Benchmark Experiments: http://icsbep.inel.gov/handbook.shtml

.. _INDC(USA)-107: http://www-nds.iaea.org/publications/indc/indc-usa-0107.pdf

.. _Monte Carlo Performance Benchmark: http://www.oecd-nea.org/dbprog/MonteCarloPerformanceBenchmark.htm

.. _OECD/NEA Source Convergence Benchmarks: http://www.oecd-nea.org/science/wpncs/convergence/specifications/index.html

.. _C5G7: https://www.oecd-nea.org/science/docs/2003/nsc-doc2003-16.pdf
