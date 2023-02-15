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
    print("libname: ", libname, " type: " , type(libname))

    # Load the shared library into c types.
    if sys.platform.startswith("win"):
        c_lib = ctypes.CDLL(libname / "cppmult.dll")
    else:
        c_lib = ctypes.CDLL(libname / "libcppmult.so")

    # Sample data for our call:
    x, y = 6, 2.3

    # This will not work:
    # answer = c_lib.cmult(x, y)

    # This produces a bad answer:
    answer = c_lib.cppmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
    print()

    # You need tell ctypes that the function returns a float
    c_lib.cppmult.restype = ctypes.c_float
    answer = c_lib.cppmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
