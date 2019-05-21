#include <Python.h>
#include <stdio.h>

/**
 *print_python_list_info - print list
 *@p: PyObject
 *Return:  No
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t tam_list, iter, alloc_1;
	PyObject *pyobject_per;
	const char *type_obj;

	tam_list = PyList_Size(p);
	alloc_1 = ((PyListObject *)p)->allocated;
	printf("[*] Python list info");
	printf("[*] Size of the Python List = %li\n", tam_list);
	printf("[*] Allocated = %li\n", alloc_1);
	for (iter = 0; iter < tam_list; iter++)
	{
		pyobject_per = PyList_GetItem(p, iter);
		type_obj = Py_TYPE(pyobject_per)->tp_name;
		printf("Element %li: %s\n", iter, type_obj);
	}
}

/**
 *print_python_bytes - print bytes
 *@p: PyObject
 *Return:  No
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t tam_list, iter, alloc_1;
	PyObject *pyobject_per;
	const char *type_obj;

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	printf("[.] bytes object info\n");
	printf("size: %d\n", size);
	printf("trying string: %s\n", string);
	if (size < 11)
		tam = size;
	else
		tam = 10;
	printf("first %d bytes:", tam);
	for (iter = 0; iter < tam_list; iter++)
	{
		printf("%x ", string[iter]);
	}
}
/**
 *print_python_float - print float
 *@p: PyObject
 *Return:  No
 */
void print_python_float(PyObject *p)
{
	Py_ssize_t tam_list, iter, alloc_1;
	PyObject *pyobject_per;
	const char *type_obj;

	tam_list = PyList_Size(p);
	alloc_1 = ((PyListObject *)p)->allocated;
	printf("[.] float object info\n");
	printf("  value: %f1.0", value);
}
