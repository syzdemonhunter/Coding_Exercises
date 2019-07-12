# T: O(n)
# S: O(n)

import collections
def invertBinaryTree(tree):
    if not tree:
		return tree
	
	q = collections.deque([tree])
	while q:
		size = len(q)
		for i in range(size):
			cur = q.popleft()
			cur.left, cur.right = cur.right, cur.left
			if cur.left:
				q.append(cur.left)
			if cur.right:
				q.append(cur.right)
				
	return tree
