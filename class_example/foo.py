import ctypes
import sys 
import pathlib 
import os 

script_dir = os.path.abspath(os.path.dirname(__file__))
libname_str = os.path.join(script_dir)
libname = pathlib.Path(libname_str)
lib = ctypes.CDLL(libname / "libfoo.so")

class Foo(object):

    def __init__(self, val):
        lib.Foo_new.argtypes = [ctypes.c_int]
        lib.Foo_new.restype = ctypes.c_void_p
        lib.Foo_bar.argtypes = [ctypes.c_void_p]
        lib.Foo_bar.restype = ctypes.c_void_p
        lib.Foo_foobar.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.Foo_foobar.restype = ctypes.c_int
        self.obj = lib.Foo_new(val)

    def bar(self):
        lib.Foo_bar(self.obj)
    
    def foobar(self, val):
        return lib.Foo_foobar(self.obj, val)

f=Foo(5)
# Calling f.bar() will print a message including the value...
f.bar()
# Now we'll use foobar to add a value to that stored in our Foo object, f
print (f.foobar(7))
# Now we'll do the same thing - but this time demonstrate that it's a normal
# Python integer...
x = f.foobar(2)
print (type(x))