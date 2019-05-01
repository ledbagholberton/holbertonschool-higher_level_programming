#include "lists.h"
/**
 * insert_nodeint_at_index - insert a node in the idx position
 *@head: head of linked list
 *@number: to be included in the   linked list
 * Return: The address of new node / NULL if fail or is not possible index
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *aux, *new, *aux1;

  aux = *head;
  new = malloc(sizeof(listint_t));
  new->n = number;  
  if (new == NULL)
    return (NULL);
  if (aux->n > number)
    {
      new->next = *head;
      *head = new;
    }
  while (aux->n  < number)
    {
      aux1 = aux;
      aux = aux->next;
    }
  aux1->next = new;
  new->next = aux;
  return (new);
}
