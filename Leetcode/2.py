# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# T: O(n)
# S: O(n)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        total = 0
        cur = dummy
        p1, p2 = l1, l2
        while p1 or p2:
            if p1:
                total += p1.val
                p1 = p1.next
                
            if p2:
                total += p2.val
                p2 = p2.next
                
            cur.next = ListNode(total%10)
            total //= 10
            cur = cur.next
            
        if total == 1:
            cur.next = ListNode(1)
        return dummy.next