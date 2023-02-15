import os
from ctypes import *

script_dir = os.path.abspath(os.path.dirname(__file__))
lib_path = os.path.join(script_dir, "libfifthy.so")

# import shared lib
libfifthy = cdll.LoadLibrary(lib_path)

# define argument types for the add_fifthy function from the shared lib
libfifthy.add_fifthy.argtypes = [POINTER(c_int), c_int]

# build python array
arr =  [1,2,3,4,5]

# allocates memory for an equivalent array in C and populates it with
# values from `arr`
arr_c = (c_int * 5)(*arr)

# Call the C function
libfifthy.add_fifthy(arr_c, c_int(5))

# original array unchanged
print('Original array: ', arr)

# this will print a reference like: <__main__.c_int_Array_5 object at 0x104e7d9e0>
print('Array altered from shared lib: ', arr_c)

# prints all the changed items in a_c
print('All values in altered array:')
for i in arr_c:
  print(i)