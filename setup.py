#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='tntorch',
    version='0.1.0',
    description="High-dimensional learning using tensor train networks",
    long_description=readme + '\n\n' + history,
    url='https://github.com/rballester/tntorch',
    author="Rafael Ballester-Ripoll",
    author_email='rballester@ifi.uzh.ch',
    packages=[
        'tntorch',
    ],
    include_package_data=True,
    install_requires=[
        'future',
        'numpy',
        'scipy',
	    'ttpy',
        # 'pytorch'
    ],
    license="LGPL",
    zip_safe=False,
    keywords='tntorch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require='nose'
)
