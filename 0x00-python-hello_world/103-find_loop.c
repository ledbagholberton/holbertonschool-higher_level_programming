#include "lists.h"

/**
 * cchek_cycle - check loop in linked lists.
 *@list: head of linked list
 *
 * Return: 1 if loop / 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *aux, *aux2;

		do {
		aux = aux->next;
		aux2 = aux2->next->next;
		if (aux == aux2)
			return (0);
		} while (aux != NULL && aux2 != NULL && aux2->next != NULL)
			return (1);
}
