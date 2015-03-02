#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    import setuptools
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()

from setuptools import setup, find_packages

try:
    import PyQt4
except ImportError:
    print("PyQt4 is not installed but is required by pyhrf_viewer.\n"
          "Please install PyQt4 before running pyhrf_viewer installation.")
    sys.exit(1)

import pyhrf_viewer

setup(
    name = "pyhrf_viewer",
    version = pyhrf_viewer.__version__,
    description = "Nifti files viewer for fMRI",
    long_description = open("README.rst").read(),
    author = ("Thomas VINCENT, Philippe CIUCIU, Florence FORBES, "
              "Solveig BADILLO, Aina FRAU, Thomas PERRET"),
    author_email = "thomas.tv.vincent@gmail.com",
    maintainer = "Thomas PERRET",
    maintainer_email = "thomas.perret@inria.fr",
    url = "https://github.com/pyhrf/pyhrf_viewer",
    packages = find_packages(),
    include_package_data = True,
    scripts = ["bin/pyhrf_view", "bin/pyhrf_xmledit"],
    install_requires = ["pyhrf", "pyqt4"],
    classifiers=[
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    license="CeCILLv2",
    platforms = ["linux"],
)
