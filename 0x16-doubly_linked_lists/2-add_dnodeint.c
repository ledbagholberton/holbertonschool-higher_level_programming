#include "lists.h"
/**
 * add_dnodeint - insert at the beginning
 *@head: head
 *@n: info
 * Return: # nodes
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new, *aux1;

	aux1 = *head;
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->prev = NULL;
	new->n = n;
	if (*head == NULL)
		new->next = NULL;
	else
	{
		aux1->prev = new;
		new->next = aux1;
	}
	*head = new;
	return (*head);
}
