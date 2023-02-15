#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import ctypes
import sys
import pathlib
import os


if __name__ == "__main__":
    # libname = pathlib.Path().absolute()
    script_dir = os.path.abspath(os.path.dirname(__file__))
    libname_str = os.path.join(script_dir)
    libname = pathlib.Path(libname_str)

    # Load the shared library into c types.
    c_lib = ctypes.CDLL(libname / "libsumm.so")

    # Sample data for our call:
    # build python array
    arr = [1,2,3,4,5,6]
    length = 6

    # allocates memory for an equivalent array in C and populates it with
    # values from `arr`
    arr_c = (ctypes.c_int * length)(*arr)
    print("arr_c: " , arr_c)

    # You need tell ctypes that the function returns a float
    c_lib.summ.restype = ctypes.c_int
    answer = c_lib.summ(arr_c, ctypes.c_int(length))
    print("arr: " , arr, " answer: " , answer)
