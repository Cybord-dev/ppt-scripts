#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from setuptools import setup, find_packages

version = "1.0.0"
author = "ntlink"

setup(
    name='ntlink',
    version=version,
    author=author,
    long_description=open('./README.txt', 'r').read(),
    packages=find_packages(),
    install_requires=[
        'boto3',
        'elementpath',
        'datetime'
    ],
    include_package_data=True,
    zip_safe=True,
)