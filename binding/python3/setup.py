import os
import sys

from setuptools import setup

# Use versioneer to set version automatically


setup(name='ezc3d',
      version=0.3.3,
      description='Easy to use C3D reader/writer in C++, Python and Matlab',
      author='Pyomeca Team',
      author_email='pariterre@gmail.com',
      url='https://github.com/pyomeca/ezc3d',
      license='MIT',
      packages=['ezc3d'],
      package_data={'ezc3d': ['_*.*', '*.dylib', '*.dll', '*.so*']},
      include_package_data=True,
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          ],
      )
