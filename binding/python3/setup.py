from setuptools import setup

setup(name='ezc3d',
      version='0.3.2',
      description='Easy to use C3D reader/writer in C++, Python and Matlab',
      author='Pariterre',
      author_email='pariterre@hotmail.com',
      url='https://github.com/pyomeca/ezc3d',
      license='MIT License',
      packages=['ezc3d'],
      install_requires=['numpy'],
      keywords='c3d', 
      package_data={'ezc3d': ['*.dylib', '*.dll', '*.so*']},
      classifiers=[
          'Programming Language :: Python :: 3',
          ],
      )
      
