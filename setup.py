#!/usr/bin/env python
"""
Setup script for PyDSTool

This uses Distutils, the standard Python mechanism for installing packages.
For the easiest installation just type::

    python setup.py install

(root privileges probably required). If you'd like to install only for local user,
type the following to install PyDSTool::

    python setup.py install --user

In addition, there are some other commands::

python setup.py clean - Clean all trash (*.pyc, emacs backups, etc.)
python setup.py test  - Run test suite

"""


from setuptools import setup, os, find_packages
from setuptools.command.test import test as TestCommand
from setuptools import Command
import sys


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def check_dependency_versions():
    assert(int(sys.version_info[0]) < 3), "PyDSTool only work with Python < 3"


class clean(Command):
    description = 'Remove build and trash files'
    user_options = [("all", "a", "the same")]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        pass

    def run(self):
        import os
        os.system(
            "rm -fr ./*.pyc ./*~ ./*/*.pyc ./*/*~ ./*/*/*.pyc ./*/*/*~ ./*/*/*.so ./PyDSTool/tests/auto_temp ./PyDSTool/tests/dopri853_temp ./PyDSTool/tests/radau5_temp ./PyDSTool/tests/dop853* ./PyDSTool/tests/radau5* ./PyDSTool/tests/*.pkl ./PyDSTool/tests/fort.9")
        os.system("rm -rf tests/radau5_temp tests/dopri853_temp radau5_temp dopri853_temp")
        os.system("rm -fr build")
        os.system("rm -fr dist")
        # os.system("rm -fr doc/_build")


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = filter(lambda a: a is not None, self.test_args)
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        import os
        os.system("rm -rf dopri853_temp radau5_temp")
        sys.exit(errno)


check_dependency_versions()
setup(
    name="PyDSTool",
    version="0.88-20130406",
    packages=find_packages(),
    install_requires=[
        "scipy>=0.9",
        "numpy>=1.6"
    ],
    tests_require=['pytest'],
    cmdclass={
        'test': PyTest,
        'clean': clean
    },
    author="Rob Clewley; W. Erik Sherwood; M. Drew Lamar",
    maintainer="Rob Clewley",
    maintainer_email="rclewley@gsu.edu",
    description=("Python dynamical systems simulation and modeling"),
    long_description = read('README.md'),
    license = "BSD",
    keywords = "dynamical systems, bioinformatics, modeling, bifurcation analysis",
    url = "http://pydstool.sourceforge.net",
    include_package_data=True,
    platforms = ["any"],
    package_data = {
        '': ['*.txt', '*.rst'],
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: Linux",
    ],
)