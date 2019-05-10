#include <Python.h>
#include <stdio.h>
/**
 *print_python_bytes -
 *@p: pyobject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, cont;
	char *string;
	int i;

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		string = PyBytes_AsString(p);
		printf("[.] bytes object info\n");
		printf("size: %li\n", size);
		printf("trying string: %s\n", string);
		if (size <= 10)
			cont = size + 1;
		else
			cont = 10;
		printf("first %li bytes: ", cont);
		i = 0;
		while (cont > 0)
		{
			printf("%02x ", string[i] & 0xFF);
			cont--;
			i++;
		}
		printf("\n");
	}
	else
		printf("[ERROR] Invalid Bytes Object\n");
}


/**
 *print_python_list -
 *@p: pyobject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t tam_list, iter, alloc_1;
	PyObject *pyobject_per;
	const char *type_obj;

	tam_list = PyList_Size(p);
	alloc_1 = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %li\n", tam_list);
	printf("[*] Allocated = %li\n", alloc_1);
	for (iter = 0; iter < tam_list; iter++)
	{
		pyobject_per = PyList_GetItem(p, iter);
//		type_obj = (((PyObject*)(pyobject_per))->tp_name)
		type_obj = Py_TYPE(pyobject_per)->tp_name;
		printf("Element %li: %s\n", iter, type_obj);
	}
}
