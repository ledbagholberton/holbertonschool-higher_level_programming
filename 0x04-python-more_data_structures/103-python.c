#include <Python.h>
#include <stdio.h>
/**
 *print_python_bytes -
 *@p: pyobject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *string;
	int cont, cont1, i;

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	for (cont = 0; string[cont] != '\0';cont++)
		;
	printf("[.] bytes object info\n");
	printf("size: %li\n", size);
	printf("trying string: %s\n", string);
	if (cont <= 10)
		cont1 = cont;
	else
		cont1 = 10;
	printf("first %d bytes: ", cont1);
	i = 0;
	while (cont1 >= 0)
	{
		printf("%x", string[i]);
		cont1--;
		i++;
	}
	printf("\n");
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
		type_obj = Py_TYPE(pyobject_per)->tp_name;
		printf("Element %li: %s\n", iter, type_obj);
	}
}

