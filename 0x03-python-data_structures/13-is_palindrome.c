/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
	listint_t aux;
	int cont;
	int buffer = 
	
	aux = *head;
	cont = 0;
	while (aux != NULL)
	{
		aux = aux->next;
		cont++;
	}
	if (cont % 2 == 0)
		cont1 = cont / 2;
	else
		cont1 = (cont - 1)/ 2;
       
	aux = *head;
	suma = 0;
	while (cont1 > 0)
	{
		aux = aux->next;
		suma = suma + aux->n;
		cont1--;
	}
	
		
