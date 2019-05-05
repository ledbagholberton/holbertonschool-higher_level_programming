#include "lists.h"

/**
 * get_dnodeint_at_index - return  the n-node
 *@head: head of linked list
 *@index: index
 * Return: n of nth node
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *aux;
	unsigned int cont;

	aux = head;
	if (head == NULL)
		   return NULL;
	if (head->next == NULL)
		return(head);
	cont = 0;
	while (aux)
	{
		if (cont == index)
			break;
		cont++;
		aux = aux->next;
	}
	if (index > cont)
		return (NULL);
	return(aux);
}
