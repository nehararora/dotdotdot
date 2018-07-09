# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_text = f.read()

setup(
    name='dotdotdot',
    version='1.0.0',
    description='Access application configuration in dot notation',
    long_description=readme,
    url='https://github.com/nehararora/dotdotdot',
    license=license_text,
    author='Nehar Arora',
    author_email='me@nehar.net',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires = [
            'PyYAML'
        ]
)
