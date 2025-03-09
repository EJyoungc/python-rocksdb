
// Include the Python C API header
#include <Python.h>

// Include RocksDB header (assumes RocksDB is installed in your environment)
#include <rocksdb/db.h>

// Example function: Return a simple string
static PyObject* get_hello(PyObject* self, PyObject* args) {
    return PyUnicode_FromString("Hello from RocksDB!");
}

// List of functions to add to the module
static PyMethodDef RocksdbMethods[] = {
    {"get_hello", get_hello, METH_NOARGS, "Return a greeting string."},
    {NULL, NULL, 0, NULL} // Sentinel to mark the end of the array
};

// Module definition
static struct PyModuleDef rocksdbmodule = {
    PyModuleDef_HEAD_INIT,
    "rocksdb",   // Module name
    "Python interface for RocksDB C++ bindings.", // Module documentation
    -1,
    RocksdbMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_rocksdb(void) {
    return PyModule_Create(&rocksdbmodule);
}
