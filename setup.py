#! /usr/bin/env python

from setuptools import setup
from os.path import join

setup(name='libroadrunner_tr',
      version='0.1.0',
      description='SBML Test Suite Runner for libRoadRunner',
      author='J. Kyle Medley',
      packages=['roadrunner_tr'],
      scripts=[join('bin','roadrunner_tr'),
      install_requires=[
        'libroadrunner',
        'pandas',
        ],
      )
