#include "lists.h"

int check(listint_t **head, listint_t *last);

/**
 * is_palindrome - know if the linked list palindrom or not
 * @head: poinrer to head
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check(head, *head));
}
/**
 * check - check if the list is palindrome
 * @head: pointer for head
 * @last: ptr to the end of the list
 * Return: 0 if not palindrom else 1
 */
int check(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
