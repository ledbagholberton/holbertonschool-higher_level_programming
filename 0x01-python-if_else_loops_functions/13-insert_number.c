#include "lists.h"
/**
 * insert_node - insert a node in the idx position
 *@head: head of linked list
 *@number: to be included in the   linked list
 * Return: The address of new node / NULL if fail or is not possible index
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *new, *aux1;

	aux = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (aux->n > number)
	{
		new->next = *head;
		*head = new;
	}
	while (aux->n  < number && aux->next != NULL)
	{
		aux1 = aux;
		aux = aux->next;
	}
	if (aux->next != NULL)
	{
		aux1->next = new;
		new->next = aux;
	}
	else
	{
		aux->next = new;
		new->next = NULL;
	}
	return (new);
}
