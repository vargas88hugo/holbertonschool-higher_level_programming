#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
  Py_ssize_t i, j, k;
  PyObject *Obj;

  i = PyList_GET_SIZE(p);
  k = ((PyListObject *)(p))->allocated; 
  printf("[*] Size of the Python List = %ld\n", i);
  printf("[*] Allocated = %ld\n", k);
  for (j = 0; j < i; j++)
    {
      Obj = PyList_GET_ITEM(p, j); 
      printf("Element %ld = %s\n", j, (char *)(((PyObject *)(Obj))->ob_type)->tp_name);
    }
}
