#!/usr/bin/env python

"""
Setup script for pdfgrep - a pdf grepping utility
"""

from setuptools import setup

with open('requirements.txt', 'r') as reqs_file:
    REQS = reqs_file.readlines()
VER = '1.0.0'

setup(
    name='indicator',
    packages=['indicator'],
    version=VER,
    description='Technical Indicator',
    author='Amro Diab',
    author_email='adiab@linuxmail.org',
    url='https://github.com/adiabuk/Technical-Inicators',
    download_url=('https://github.com/adiabuk/Technical-Indicators/archive/{0}.tar.gz'
                  .format(VER)),
    keywords=['pdf', 'grep'],
    install_requires=REQS,
    test_suite='tests.test_pdfgrep',
    classifiers=[],
)
