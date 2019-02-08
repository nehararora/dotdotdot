# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_text = f.read()

setup(
    name='dotdotdot',
    version='1.0.0',
    description='Access application configuration using dot notation',
    long_description=readme,
    long_descritpion_content_type='text/markdown; charset=UTF-8',
    url='https://github.com/nehararora/dotdotdot',
    license=license_text,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries',
    ],
    author='Nehar Arora',
    author_email='me@nehar.net',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
            'PyYAML'
        ]
)
