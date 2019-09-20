#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
  Py_ssize_t i, j;
  /* PyObject *Obj; */
  char * str;

  i = ((PyVarObject *)(p))->ob_size;
  str = ((PyBytesObject *)(p))->ob_sval;

  printf("[.] bytes object info\n");
  if (_pyObject_CAST(p)->ob_type == &PyBytes_Type)
    {
      printf("[ERROR] Invalid Bytes Object\n");
      return;
    }
  printf("  size: %ld\n", i);
  printf("  trying string: %s\n", str);

  if (i > 10)
    i = 10;
  printf("  first %ld bytes:", i);

  for (j = 0; j < i; j++)
    {
      printf(" %02x", (unsigned)(unsigned char)str[j]);
    }
  putchar(10);
}

void print_python_list(PyObject *p)
{
  Py_ssize_t i, j, k;
  PyObject *Obj;

  i = ((PyVarObject *)(p))->ob_size;
  j = ((PyListObject *)(p))->allocated;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", i);
  printf("[*] Allocated = %ld\n", j);

  for (k = 0; k < i; k++)
    {
      Obj = ((PyListObject *)(p))->ob_item[k];
      printf("Element %ld: %s\n", j, (char *)((PyObject *)(Obj))->ob_type->tp_name);
    }
}
