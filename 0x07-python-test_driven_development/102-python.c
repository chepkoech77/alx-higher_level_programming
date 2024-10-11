#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Invalid Python string object\n");
        return;
    }

    Py_UNICODE *unicode_str = PyUnicode_AsUnicode(p);
    Py_ssize_t length = PyUnicode_GetLength(p);

    printf("String: %ls\n", unicode_str);
    printf("Length: %zd\n", length);
}
