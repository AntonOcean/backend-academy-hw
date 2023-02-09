#ifndef __LIBMYPY_H__
#define __LIBMYPY_H__

#include <Python.h>

/* PyObject на самом деле является просто объектом Python на уровне C и определен в Python.h */
PyObject * hello(PyObject *);

#endif