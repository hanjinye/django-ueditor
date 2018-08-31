#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-ueditor',
    description=(
        'Qitian Inc. Django UEditor plugins. For quick use in Django Admin Panel'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.0.1',
    author='Peter Han',
    author_email='peter@qitian.com',
    url='https://www.qitian.biz/',
    license='MIT License',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'django>=2.0'
    ],
    python_requires=">=3.6, !=3.0.*",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Utilities',
    ],
)
