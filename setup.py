#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
import codecs
from setuptools import setup, find_packages
from ip138 import __version__, __author__, __email__

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]


def long_description():
    with codecs.open('README.rst', 'rb') as readme:
        if not sys.version_info < (3, 0, 0):
            return readme.read().decode('utf-8')


setup(
    name='iip-138',
    version=__version__,
    author='Qoo-330ml',
    author_email='opensource@users.noreply.github.com',
    description='IP 地理位置信息查询工具（适配 ipshudi 页面）',
    long_description=long_description(),
    keywords=['ip138', 'ip', 'geolocation'],
    maintainer='Qoo-330ml',
    maintainer_email='opensource@users.noreply.github.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Qoo-330ml/ip138',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'iip-138 = ip138.command:main',
            'ip138 = ip138.command:main',
        ]
    },
)
