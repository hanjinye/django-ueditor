#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import sys

version = '0.0.3'

long_description = "\n".join([
    open('README.md', 'r').read(),
])

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()


setup(
    name='django-ueditor',
    description=(
        'Qitian Inc. Django UEditor plugins. For quick use in Django Admin Panel'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='django wysiwyg editor widget ueditor',
    version=version,
    author='Peter Han',
    author_email='peter@qitian.com',
    url='https://www.qitian.biz/',
    license='MIT License',
    packages=find_packages(exclude=['test_ueditor']),
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
    zip_safe=False,
)
