#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='SpyPhisher',
    version=version,
    description='A python phishing script for login phishing, image phishing video phishing an many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Spyder',
    author_email='portable36@gmail.com',
    license="GPLv3",
    url='https://github.com/portable36/SpyPhisher',
    scripts=['spyphisher'],
    install_requires=["requests", "bs4"]
)
