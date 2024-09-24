#include "lists.h"
/**
 * check_cycle - function to check cycle
 * @list: list
 *
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
