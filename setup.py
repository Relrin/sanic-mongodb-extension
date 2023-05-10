# -*- coding: utf-8 -*-
import os
import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')
requirements = [
    'sanic-base-extension==0.2.0',
    'motor==3.1.2',
    'umongo==3.1.0',
]


with open('sanic_mongodb_ext/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, '__init__.py'))
    ]


setup(
    name='sanic-mongodb-extension',
    version=version,
    url='https://github.com/Relrin/sanic-mongodb-extension',
    license='BSD',
    author='Valeryi Savich',
    author_email='relrin78@gmail.com',
    description='MongoDB with μMongo ODM support for Sanic framework',
    long_description=read('README.rst'),
    packages=get_packages('sanic_mongodb_ext'),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
