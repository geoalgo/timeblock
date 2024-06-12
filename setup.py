from setuptools import setup, find_packages

setup(
    name='timeblock',
    version='0.0.1',
    packages=find_packages(exclude='tst'),
    url='https://github.com/geoalgo/timeblock',
    license='Apache-2.0',
    author='geoalgo',
    extras_require={"dev": "pytest"},
    description='A simple implementation for embarrassingly parallel for supporting multiple backends.',
)
