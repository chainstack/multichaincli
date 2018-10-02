#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = ['']


setup(name='multichaincli',
    version='1.0.5',
    description='A python binding for Multichain Json-RPC API',
    long_description=read('README.md'),
    license="BSD",
    author='Alex Khaerov, Federico Cardoso',
    author_email='alex.khaerov@chainstack.com, federico.cardoso@dxmarkets.com',
    url='https://github.com/chainstack/multichain-python-sdk',
    keywords='multichain python blockchain jsonrpc',
    packages=find_packages(),
    install_requires=[
        'requests==2.19.1',
    ],
    )
