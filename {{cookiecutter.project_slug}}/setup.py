#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from pip.req import parse_requirements
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def get_requirements(file_name):
    full_path = path.dirname(path.abspath(__file__))
    full_path = path.join(full_path, 'requirements', file_name)
    reqs = parse_requirements(full_path, session=False)
    return [str(ir.req) for ir in reqs]

requirements = get_requirements('stable.txt') + get_requirements('experimental.txt')
test_requirements = get_requirements('test.txt')

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(exclude=[
        '{{cookiecutter.project_slug}}_tests',
        '{{cookiecutter.project_slug}}_tests.*'
    ]),
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='{{cookiecutter.project_slug}}_tests',
    tests_require=test_requirements
)
