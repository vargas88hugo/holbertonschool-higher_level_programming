#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>
#include <floatobject.h>
#include <string.h>
#include <float.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
  Py_ssize_t i, j, k;
  PyObject *Obj;

  i = ((PyVarObject *)(p))->ob_size;
  j = ((PyListObject *)(p))->allocated;

  printf("[*] Python list info\n");

  if (((PyObject *)(p))->ob_type != &PyList_Type)
    {
      printf("  [ERROR] Invalid List Object\n");
      return;
    }

  printf("[*] Size of the Python List = %ld\n", i);
  printf("[*] Allocated = %ld\n", j);

  fflush(stdout);

  for (k = 0; k < i; k++)
    {
      Obj = ((PyListObject *)(p))->ob_item[k];
      printf("Element %ld: %s\n", k, (char *)((PyObject *)(Obj))->ob_type->tp_name);

      if (strcmp(((PyObject *)(Obj))->ob_type->tp_name, "bytes") == 0)
	print_python_bytes(Obj);
      else if (strcmp(((PyObject *)(Obj))->ob_type->tp_name, "float") == 0)
	print_python_float(Obj);
    }
}

void print_python_bytes(PyObject *p)
{
  Py_ssize_t i, j;
  char * str;

  i = ((PyVarObject *)(p))->ob_size;
  str = ((PyBytesObject *)(p))->ob_sval;

  printf("[.] bytes object info\n");

  if (strcmp(((PyObject *)(p))->ob_type->tp_name, "bytes") != 0)
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  printf("  size: %ld\n", i);
  printf("  trying string: %s\n", str);

  if (i >= 10)
    i = 9;
  printf("  first %ld bytes:", i + 1);

  for (j = 0; j <= i; j++)
    {
      printf(" %02x", (unsigned)(unsigned char)str[j]);
    }
  putchar(10);
}

void print_python_float(PyObject *p)
{
  long double i;
  char buff[100];
  int j, k;

  printf("[.] float object info\n");

  if (strcmp(((PyObject *)(p))->ob_type->tp_name, "float") != 0)
    {
      printf("  [ERROR] Invalid Float Object\n");
      return;
    }

  i = ((PyFloatObject *)(p))->ob_fval;
  gcvt(i, 20, buff);

  for (j = 0; buff[j]; j++)
    if (buff[j] == '.')
      k = 1;

  if (k != 1)
    printf("  value: %s.0\n", buff);
  else
    printf("  value: %s\n", buff);
}
