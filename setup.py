#!/usr/bin/env python
# coding=utf-8

from setuptools import find_packages, setup

setup(
    name="git_sew",
    version="0.0.1",
    description="",
    long_description="",
    entry_points={
        "console_scripts": [
            "fixup-editor=git_sew.fixup:fixup_editor",
            "git-fixup=git_sew.fixup:fixup",
            "git-sew=git_sew.ui.cli.main:main",
        ]
    },
    classifiers=[
        # See https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="git",
    author="Flavio Curella",
    author_email="flavio.curella@gmail.com",
    url="",
    license="MIT License",
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    platforms=["any"],
    test_suite="tests",
    setup_requires=["pytest-runner"],
    install_requires=[
        "click>=7.0",
        "frozendict>=1.2",
        "gitpython>=3.0.2",
        "urwid-pydux>=0.2.0",
    ],
    tests_require=["pytest"],
)
