#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists, dirname, realpath
from setuptools import setup, find_packages
import sys


# temaplte originally by Eoghan O'Connell at
#   https://github.com/PinkShnack/template_python_repo
maintainer = "Eoghan O'Connell"
maintainer_email = "eoghan.oconnell@mpl.mpg.de"
description = 'StAP (statistics and probability) repository from the GuckLab.'
name = "StAP"
year = "2022"
url = 'https://github.com/GuckLab/StAP'
license = "MIT"

sys.path.insert(0, realpath(dirname(__file__))+"/"+name)
from _version import version  # noqa: E402


setup(
    name=name,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    url=url,
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license=license,
    description=description,
    long_description=open('README.md').read() if exists('README.md') else '',
    install_requires=[
        "numpy>=1.21.0",
        "jupyter>=1.0.0",
        "matplotlib>=3.5.0",
        ],
    python_requires=">=3.7",
    keywords=["template"],
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Topic :: Scientific/Engineering :: Mathematics',
                 'Intended Audience :: Education',
                 ],
    platforms=['ALL'],
    )
