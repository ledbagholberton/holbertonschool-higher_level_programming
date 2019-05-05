#include "lists.h"
/**
 * dlistint_len - print len elements of list double link
 *@h: head
 *
 * Return: # nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t a;

	a = 0;
	while (h != NULL)
	{
		a++;
		h = (*h).next;
	}
	return (a);
}
