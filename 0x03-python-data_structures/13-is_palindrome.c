#include "lists.h"

void cpy_reverse(listint_t **head1, listint_t *head2);

/**
 * is_palindrome - function that checks if the list is palindrome or not
 * @head: Head of the linked list
 * Return: 1 if it is palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL, *cpy = NULL;
	int i = 1;

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	for (; temp; temp = temp->next)
	        cpy_reverse(&cpy, temp);

	temp = *head;

	for (; temp; temp = temp->next, cpy = cpy->next)
		if (temp->n != cpy->n)
			i = 0;

	return (i);
}

/**
 * append - function that copies a linked list
 * @head1: Head of the copy linked list
 * @head2: Head of the linked list to be copied
 */
void cpy_reverse(listint_t **head1, listint_t *head2)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return;

	if (*head1 == NULL)
	{
		*head1 = new;
		new->n = head2->n;
		new->next = NULL;
		return;
	}

        new->n = head2->n;
	new->next = *head1;
	*head1 = new;
}
