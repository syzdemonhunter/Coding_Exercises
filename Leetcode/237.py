# https://leetcode.com/problems/delete-node-in-a-linked-list/
# T: O(1)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return
        node.val = node.next.val
        node.next = node.next.next