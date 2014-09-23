#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pyaltmetric',
    version='0.2.0',
    packages=['pyaltmetric'],
    description='Python Altmetric API v1 wrapper',
    long_description=open('README.rst').read(),
    author='Will Earp',
    author_email='will.earp@icloud.com',
    url='https://github.com/wearp/pyaltmetric',
    install_requires=['requests'],
    license="BSD",
    zip_safe=True,
    keywords='Altmetric altmetric altmetrics api wrapper',
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
