# https://leetcode.com/problems/rotate-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        index = head
        length = 1
        while index.next:
            index = index.next
            length += 1
            
        index.next = head
        for i in range(1, length - k % length):
            head = head.next
            
        result = head.next
        head.next = None
        return result
        