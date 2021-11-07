#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="cockroachDB",
    description="How to connect cockroachDB to a Django application.",
    version='3.2.5',
    url="",
    author="Oruko Pius",
    author_email="test@user.com",
    license="MIT",
    packages=find_packages(),
    install_requires=("Django>=3",),
)
