#include <Python.h>
#include <stdio.h>

/**
 *
 *
 */

void print_python_list_info(PyObject *p)
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

/**
 *
 *
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t tam_list, iter, alloc_1;
        PyObject *pyobject_per;
        const char *type_obj;

        tam_list = PyList_Size(p);
        alloc_1 = ((PyListObject *)p)->allocated;
        printf("[.] float object info\n");
	printf("value: %f1.0\n", value);
	printf("trying string: %s\n", string);
	printf("first %d bytes:");
        for (iter = 0; iter < tam_list; iter++)
        {
                pyobject_per = PyList_GetItem(p, iter);
                type_obj = Py_TYPE(pyobject_per)->tp_name;
                printf("Element %li: %s\n", iter, type_obj);
        }
}

/**
 *
 *
 */
void print_python_float(PyObject *p)
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
