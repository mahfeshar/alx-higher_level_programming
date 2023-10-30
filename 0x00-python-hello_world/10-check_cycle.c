#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *nextlist = list;
	listint_t *last = list;

	while (list && nextlist && nextlist->next)
	{
		list = list->next;
		nextlist = nextlist->next->next;

		if (list == nextlist)
		{
			list = last;
			last =  nextlist;
			while (1)
			{
				nextlist = last;
				while (nextlist->next != list && nextlist->next != last)
				{
					nextlist = nextlist->next;
				}
				if (nextlist->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}

