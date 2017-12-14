# -*- coding: utf-8 -*-
"""
Version reader/writer for popular package managers
"""
__copyright__ = "Copyright (C) Veritas LLC. All rights reserved."

# std-lib imports
import os
from setuptools import (
        setup,
        find_packages,
        )
from pip.req import parse_requirements
from pip.download import PipSession

install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]


def read_md(fname):
    """
    Get long description from README file
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='versioner',
    version='0.0.1',
    author='prathamesh.nevagi@veritas.com',
    description='Version reader/writer for popular package managers',
    long_description=read_md('README.md'),

    url='https://github.com/VeritasOS/versioner',
    download_url='https://github.com/VeritasOS/versioner.git',

    package_dir={'versioner': 'versioner'},
    packages=find_packages("."),
    package_data={'': ['README.md']},

    entry_points={
        'console_scripts': ['versioner=versioner.cli:CLI'],
        },

    install_requires=reqs,
    zip_safe=False,
)
