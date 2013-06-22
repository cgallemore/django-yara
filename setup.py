#!/usr/bin/env python

import os
import sys
from setuptools import setup


def publish():
    os.system('python setup.py sdist upload')

if sys.argv[-1] == 'publish':
    publish()
    sys.exit()

install_requires = []

setup(
    name='django-yara',
    version='0.1.0',
    description='Yet another registration app.',
    long_description=open('README.rst').read(),
    author='Chad Gallemore',
    author_email='cgallemore@gmail.com',
    url='https://github.com/cgallemore/django-yara',
    license='MIT',
    keywords='django signup registration',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ),
    packages=['yara'],
    install_requires=install_requires,
)
