# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "ts-lib-task-script-utils"
VERSION = "1.0.0"

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "numpy",
    "arrow>=0.15.8",
    "dateparser>=0.7.6"
]

setup(
    name=NAME,
    version=VERSION,
    description="Python utility functions to help write efficient Tetra Task Scripts",
    author="TetraScience",
    author_email="",
    url="",
    keywords=[],
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    long_description=readme,
    long_description_content_type="text/markdown"
)
