#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='drivewealth',
    version='1.0',
    description='Python wrapper around the DriveWealth API',
    author='Misael G.',
    author_email='hi@misalabs.com',
    install_requires=[
        "cachetools==2.0.1",
        "hammock==0.2.4",
        "marshmallow==3.0.0b8"
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
