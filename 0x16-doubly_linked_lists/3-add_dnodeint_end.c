#include "lists.h"

/**
 * add_dnodeint_end - add new node at the end
 *@head: head of linked list
 *@n: number in new node
 *
 * Return: addres of new element
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new, *aux;

	aux = *head;
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (aux != NULL)
	{
		while (aux->next != NULL)
			aux = aux->next;
		new->prev = aux;
		aux->next = new;
	}
	else
	{
		new->prev = NULL;
		*head = new;
	}
	return (new);
}
