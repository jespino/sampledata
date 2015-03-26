#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = 'sampledata',
    version = ":versiontools:sampledata:",
    description = "Helper class for generate sample data",
    long_description = "",
    keywords = 'sample, data, example, loremipsum',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/jespino/sampledata',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    package_data={
        'sampledata': ['static/*', 'l10n/names/*',]
    },
    install_requires=[
        'six',
        'pytz',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    test_suite = 'nose.collector',
    tests_require = ['nose >= 1.3.0'],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
