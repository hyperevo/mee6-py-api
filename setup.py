#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)


setup(
    name='mee6_py_api',
    version='0.0.1',
    description="""Unofficial Python API for the Mee6 Discord bot""",
    long_description_markdown_filename='README.rst',
    author='Tommy Mckinnon',
    author_email='admin@hyperevo.com',
    url='https://github.com/hyperevo/mee6-py-api',
    include_package_data=True,
    install_requires=[
        "aiohttp>=3,<4",
    ],
    setup_requires=['setuptools-markdown'],
    python_requires='>=3.6,<4',
    license="MIT",
    zip_safe=False,
    keywords='mee6 python api',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)