import ctypes
import sys
import pathlib
import os
from numpy.ctypeslib import ndpointer

libname = pathlib.Path().absolute()
script_dir = os.path.abspath(os.path.dirname(__file__))
libname_str = os.path.join(script_dir)
libname = pathlib.Path(libname_str)
lib = ctypes.CDLL(libname / "libarr.so")
lib.arr_return.restype = ndpointer(dtype=ctypes.c_int, shape=(10,))
res = lib.arr_return()
print("res type: " , type(res))
print("res: " , res)