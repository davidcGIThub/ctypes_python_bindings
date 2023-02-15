#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import numpy as np
import ctypes
import pathlib
import os

script_dir = os.path.abspath(os.path.dirname(__file__))
libname_str = os.path.join(script_dir)
libname = pathlib.Path(libname_str)

math_lib = ctypes.CDLL(libname / "libmath_operations.so")

addend_1 = ctypes.c_int(3)
addend_2 = ctypes.c_int(7)
math_lib.add_ints.restype = ctypes.c_int
answer_1 = math_lib.add_ints(addend_1, addend_2)
print(addend_1, " + " , addend_2 , " = " , answer_1)

factor_1 = ctypes.c_double(3)
factor_2 = ctypes.c_double(7)
math_lib.multiply_doubles.restype = ctypes.c_double
answer_2 = math_lib.multiply_doubles(factor_1, factor_2)
print(factor_1, " + " , factor_2 , " = " , answer_2)

array_length = 6
array = np.arange(array_length) + 1
c_array = (ctypes.c_float * array_length)(*array)
math_lib.mean_floats.restype = ctypes.c_float
answer_3 = math_lib.mean_floats(c_array, array_length)
print("mean(" , array , ")" , " = " , answer_3)
