#!/usr/bin/env python
from setuptools import setup
import envycontrol_VFIO


setup(
    name='envycontrol_With_VFIO ',
    version=envycontrol.VERSION,
    description='Easy GPU switching for Nvidia Optimus laptops under Linux',
    url='https://github.com/Maziar123/envycontrol_With_VFIO',
    author='Victor Bayas with branch of Maziar ',
    author_email='victorsbayas@gmail.com & maziar mnavahan3@gmail.com',
    license='MIT',
    py_modules=['envycontrol_With_VFIO'],
    entry_points={
        'console_scripts': [
            'envycontrol=envycontrol:main',
        ],
    },
    keywords=['nvidia', 'optimus', 'prime', 'gpu', 'linux'],
    classifiers=[
        'Development Status :: TST ONLY',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux'
    ],
)