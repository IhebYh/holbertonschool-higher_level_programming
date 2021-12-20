#include "lists.h"
/**
 * check_cycle - checking if there's a cycle in a given linked list
 * @list: listint_t
 * Return: 0 || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *_fast = list, *_slow = list;

	while (_fast && _slow && _fast->next)
		{
					_slow = _slow->next;
					_fast = _fast->next->next;
					if (_fast == _slow)
					{
						return (1);
					}
		}
	return (0);
}
