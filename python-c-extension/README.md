# Introduction

Notes of build C extension for Python based on [Building a Python C Extension
Module][1].

C extensions serve the following purposes:
- accelarating module execution speed, accelarator module usually has its pure
  python equivalent which the Python interpreter can fall back when the
  accelarating module is unavailable on a particular platform
- wrapping existing C library to offer a Pythonic programming interface
- accessing low-level system calls

Developing a C extension involves:

- Call C functions from Python
- Pass arguments from Python to C and parse them accordingly
- Raise exceptions from C code and create custom Python exceptions in C
- Define global constants in C and make them accessible in Python
- Test, package, and distribute Python C extension module

## key elements

module --> PyModuleDef --> PyMethodDef --> c funtion

## basic procedure

- define the underlying c function, use PyObject pointer to receive
object handle and parameters from Python, return PyObject pointer to
Python.
- extract arguments using `PyArg_ParseTuple`
- wrap return value using `PyLong_FromLong` etc
- describe method meta-data using PyMethodDef
- describe module meta-data using PyModuleDef
- wrap meta-data and extention method in PyMODINIT_FUNC
- write setup.py to build the extension

## define exceptions

Use `PyErr_SetString()` to raise standard exception.
For example, to raise ValueError:

    PyErr_SetString(PyExc_ValueError, "xxxx")

You can also define your own exception in C:

    static PyObject *XXXError = NULL;
    XXXError = PyExc_NewException("mod.XXXError", "descriptive message");
    PyModule_AddObject(module, "XXXError", XXXError);


## define constants or macros
Use the `PyModule_AddIntConstant` or `PyModule_AddStringConstant`
to add constants:

    PyModule_AddIntConstant(module, "XXX_FLAG", 100);

Or you can define macro first, then use `PyModule_AddIntMacro` or
`PyModule_AddStringMacro`:

    #define XXX_MACRO1 42
    #define XXX_MACRO2 "Forty-Two"
    PyModule_AddIntMacro(module, XXX_MACRO1);
    PyModule_AddStringMacro(module, XXX_MACRO2);

## Alternatives

- ctypes: included in the Python standard library
- cffi: more Pythonic
- swig
- boost::Py

[1]: https://realpython.com/build-python-c-extension-module/
