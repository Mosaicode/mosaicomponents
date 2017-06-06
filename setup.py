#!/usr/bin/env python
# -*- coding: utf-8 -*-
from glob import glob

DISTUTILS_DEBUG = "True"


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {}

config['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Code Generators',
]

setup(name='mosaicomponents',
      install_requires=['pip', 'Python>=2.7'],
      version='1.0a7',
      tests_require=['pytest'],
      test_suite='test',
      packages=['mosaicomponents'],
      description='GUI components to develop Mosaicode',
      author='Ouroboros',
      author_email='cmagnobarbosa+harpia@gmail.com',
      maintainer="Ouroboros",
      maintainer_email="cmagnobarbosa+harpia@gmail.com",
      license="GNU GPL3",
      url='http://ges.dcomp.ufsj.edu.br/index.php/ouroboros/',
      **config
      )
