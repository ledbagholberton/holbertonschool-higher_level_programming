#include "lists.h"

/**
 * free_dlistint - delete & free list double
 *@head: head of linked list
 *
 * Return: Nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *aux;

	aux = head;
	while (head)
	{
		aux = head;
		free(head);
		head = aux->next;
	}
}
