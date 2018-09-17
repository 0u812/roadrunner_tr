#! /usr/bin/env python

from setuptools import setup
from os.path import join

setup(name='libroadrunner-tr',
      version='0.1.4',
      description='SBML Test Suite Runner for libRoadRunner',
      author='J. Kyle Medley',
      packages=['roadrunner_tr'],
      #package_dir={'roadrunner_tr': 'roadrunner_tr'},
      scripts=[join('scripts','roadrunner_tr')],
      install_requires=[
        'libroadrunner',
        'pandas',
        ],
      )
