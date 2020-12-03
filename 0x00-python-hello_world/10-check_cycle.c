#include "lists.h"
/**
 * check_cycle - checks wether a single linked list has a cycle or not
 * @list: pointer to linked list
 * Return: 0 if not, 1 if it does
*/
int check_cycle(listint_t *list)
{
    listint_t *tmp1, *tmp2;

	tmp1 = list;
	tmp2 = list;

	while (tmp2->next != NULL && tmp1->next->next != NULL)
	{
		tmp2 = tmp2->next;
		tmp1 = tmp1->next->next;
		if (tmp1 == tmp2)
			return (1);
	}

	return (0);
}
