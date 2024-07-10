# from setuptools import setup
from Cython.Build import cythonize
from distutils.core import setup
from distutils.extension import Extension
import numpy as np

setup(ext_modules=cythonize(
    Extension(
        'cytree', ['cytree.pyx'],
        extra_compile_args=['-O3', '-std=c++20'], 
        include_dirs=[np.get_include()]
        ),
    ),
)
