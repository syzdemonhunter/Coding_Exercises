# https://leetcode.com/problems/reorder-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        dummy = ListNode(0)
        dummy.next = head
        tmp = None
        slow, fast = head, head
        l1 = head
        while fast and fast.next:
            tmp = slow
            slow = slow.next
            fast = fast.next.next
        tmp.next = None
        
        l2 = self.reverse(slow)
        self.merge(l1, l2)
        
    def reverse(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev
    
    def merge(self, l1, l2):
        while l1 != l2:
            n1 = l1.next
            n2 = l2.next
            l1.next = l2
            if not n1:
                break
            l2.next = n1
            l1 = n1
            l2 = n2
        
        