#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pyaltmetric',
    version='0.1',
    description='Python Altmetric API v1 wrapper',
    long_description=open('README.rst').read(),
    author='Will Earp',
    author_email='will.earp@icloud.com',
    url='https://github.com/wearp/pyaltmetric',
    install_requires=['requests'],
    license="BSD",
    zip_safe=False,
    keywords='Altmetric altmetrics api wrapper',
    test_suite='tests',
)
