#include "lists.h"
/**
 * is_palindrome - define if the linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome/ 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux;
	int cont, suma, pos;

	aux = *head;
	cont = 0;
	while (aux != NULL)
	{
		aux = aux->next;
		cont++;
	}
	pos = 1;
	suma = 0;
	aux = *head;
	while (pos <= cont / 2)
	{
		suma = suma + pos * aux->n;
		aux = aux->next;
		pos++;
	}
	pos--;
	if (cont % 2 == 0)
	{
		while (pos > 0)
		{
			suma = suma - pos * aux->n;
			aux = aux->next;
			pos--;
		}
	}
	else
	{
		aux = aux->next;
		while (pos > 0)
		{
			suma = suma - pos * aux->n;
			aux = aux->next;
			pos--;
		}
	}
	if (suma == 0)
		return (1);
	return (0);
}
