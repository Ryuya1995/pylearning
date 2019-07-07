cdef extern from "fibc.c":
    long q()

def g():
    return q()

# python fib_setup.py build_ext --inplace