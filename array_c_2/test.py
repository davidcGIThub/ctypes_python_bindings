# 
# test.py
# 
from ctypes import CDLL, POINTER
from ctypes import c_size_t, c_double
import numpy as np

# load the library
mylib = CDLL("mylib.so")
# C-type corresponding to numpy array 
ND_POINTER_1 = np.ctypeslib.ndpointer(dtype=np.float64, 
                                      ndim=1,
                                      flags="C")
# define prototypes
mylib.print_array.argtypes = [ND_POINTER_1, c_size_t]
mylib.print_array.restype = None
# create array X = [1 1 1 1 1]
X = np.ones(5)
# call function
mylib.print_array(X, X.size)