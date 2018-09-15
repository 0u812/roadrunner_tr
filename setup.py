#! /usr/bin/env python

from setuptools import setup

setup(name='libroadrunner_tr',
      version='0.1.0',
      description='SBML Test Suite Runner for libRoadRunner',
      author='J. Kyle Medley',
      packages=['roadrunner_tr'],
      install_requires=[
        'libroadrunner',
        ],
      )
