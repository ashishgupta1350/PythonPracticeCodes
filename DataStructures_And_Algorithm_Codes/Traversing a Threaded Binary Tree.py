
struct Node* leftMost(struct Node *n)
{
	if (n == NULL)
	return NULL;

	while (n->left != NULL)
		n = n->left;

	return n;
}


void inOrder(struct Node *root)
{
	struct Node *cur = leftmost(root);
	while (cur != NULL)
	{
		printf("%d ", cur->data);

		if (cur->rightThread)
			cur = cur->rightThread;
		else
			cur = leftmost(cur->right);
	}
}
