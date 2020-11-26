#!/usr/bin/env python
# Python Imports
from setuptools import setup, find_packages
# Third-Party Imports
# Project Imports


setup(
    name="Flexceptions",
    version="0.1.1",
    description="Python Flexible Exceptions Library",
    author="Alejandro Cabeza Romero",
    author_email="alex@alexcabeza.io",
    packages=find_packages(exclude=("*tests",)),
    python_requires=">=3.8",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
