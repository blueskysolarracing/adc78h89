#!/usr/bin/env python3

from setuptools import find_packages, setup

with open('README.rst', 'r') as file:
    long_description = file.read()

setup(
    name='adc78h89',
    version='0.0.0.dev1',
    description='A Python driver for Texas Instruments ADC78H89 7-Channel, 500 KSPS, 12-Bit A/D Converter',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/blueskysolarracing/adc78h89',
    author='Blue Sky Solar Racing',
    author_email='blueskysolar@studentorg.utoronto.ca',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords=[
        'python',
    ],
    project_urls={
        'Documentation': 'https://adc78h89.readthedocs.io/en/latest/',
        'Source': 'https://github.com/blueskysolarracing/adc78h89',
        'Tracker': 'https://github.com/blueskysolarracing/adc78h89/issues',
    },
    packages=find_packages(),
    install_requires=[
         'python-periphery>=2.4.1,<3',
    ],
    python_requires='>=3.11',
    package_data={'adc78h89': ['py.typed']},
)
