#!/usr/bin/env python

from setuptools import setup

setup(name='icsbep',
      version='0.1',
      description='ICSBEP',
      author='Paul Romano',
      author_email='paul.k.romano@gmail.com',
      packages=['icsbep'],
      package_data={'icsbep': ['uncertainties.csv']})
