#include "lists.h"

/**
 * insert_node - insert number at sorted linked list
 *
 * @head: pointer to head at list
 * @number: the number that I want to add
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h = *head;
	listint_t *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (h == NULL)
		*head = new;

	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}

	new->next = h;
	if (h == *head)
		*head = new;
	else
		prev->next = new;
	return (new);
}
