# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# T: O(n)
# S: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        return self.to_bst(head, None)
    
    def to_bst(self, head, tail):
        if head == tail:
            return None
        
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.to_bst(head, slow)
        root.right = self.to_bst(slow.next, tail)
        return root
            
        
        