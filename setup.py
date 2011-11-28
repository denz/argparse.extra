#!/usr/bin/env python

# Bootstrap installation of Distribute
from importlib import import_module
import distribute_setup
distribute_setup.use_setuptools()

import os

from setuptools import setup

def package_env(file_name, strict=False):
    file_path = os.path.join(os.path.dirname(__file__),file_name)
    if os.path.exists(file_path) or strict:
        return open(file_path).read()
    else:
        return u''

PACKAGE = 'argparse.extra'
PROJECT = u'argparse.extra'

VERSION = package_env('VERSION')
URL = package_env('URL')
AUTHOR, AUTHOR_EMAIL = [v.strip('>').strip() for v \
                        in package_env('AUTHOR').split('<mailto:')]
DESC = "Additional classes for argparse"

setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    long_description=package_env('README.rst'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=package_env('LICENSE'),
    namespace_packages=['argparse',],
    packages=['argparse','argparse.extra'],
    package_dir = {'argparse': 'argparse',
                   'argparse.extra':'argparse/extra'},
    include_package_data=True,
    zip_safe=True,
    test_suite = 'tests',
    install_requires=[
    ],
    classifiers=[
        # see http://pypi.python.org/pypi?:action=list_classifiers
        # -*- Classifiers -*- 
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
)

