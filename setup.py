#!/usr/bin/env python
#
# pgrepup - Upgrade PostgreSQL using logical replication
#
# Copyright (C) 2016 Denis Gasparin <denis@gasparin.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Upgrade PostgreSQL using logical replication
Pgrepup is an open-source tool written in Python for performing a major version upgrade between
two PostgreSQL clusters.
Pgrepup is distributed under GNU GPL 3 and maintained by Denis Gasparin.
"""

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 6):
    raise SystemExit('ERROR: Barman needs at least python 2.6 to work')

# Depend on pytest_runner only when the tests are actually invoked
needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []

setup_requires = pytest_runner

install_requires = [
    'psycopg2 >= 2.4.2',
    'docopt >= 0.6.0',
    'python-dateutil',
    'clint >= 0.5.1',
    'cryptography'
]

if sys.version_info < (2, 7):
    install_requires += [
        'argparse',
    ]

pgrepup = {}
with open('pgrepup/version.py', 'r') as fversion:
    exec(fversion.read(), pgrepup)

setup(
    name='pgrepup',
    version=pgrepup['__version__'],
    author='Denis Gasparin',
    author_email='denis@gasparin.net',
    url='https://www.github.com/rtshome/pgrepup',
    packages=['pgrepup', ],
    scripts=['bin/pgrepup', ],
    data_files=[],
    license='GPL-3.0',
    description=__doc__.split("\n")[0],
    long_description="\n".join(__doc__.split("\n")[2:]),
    install_requires=install_requires,
    platforms=['Linux', 'Mac OS X'],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Database',
        'Topic :: System :: Recovery Tools',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    setup_requires=setup_requires,
    tests_require=[],
)
