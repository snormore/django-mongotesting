#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-mongotesting',
    version='1.0.0-beta',
    description='An extension to the Django web framework that provides testing support for mongoengine dependent modules.',
    author='Steven Normore',
    author_email='snormore@gmail.com',
    long_description=open('README.md', 'r').read(),
    url='http://github.com/snormore/django-mongotesting/',
    packages=[
        'mongotesting',
    ],
)
