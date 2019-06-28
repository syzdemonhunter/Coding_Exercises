# https://leetcode.com/problems/plus-one-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
# T: O(n)
# S: O(1)

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        i, j = dummy, dummy
        
        while j.next:
            j = j.next
            if j.val != 9:
                i = j
                
        i.val += 1
        i = i.next
        while i:
            i.val = 0
            i = i.next
            
        if dummy.val == 0:
            return dummy.next
        return dummy
'''
# T: O(n)
# S: O(1)

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        head = self.reverse(head)
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        carry = 1
        while carry > 0 or cur.next:
            if cur.next:
                cur = cur.next
                carry += cur.val
                cur.val = carry % 10
                carry //= 10
            else:
                cur.next = ListNode(carry)
                cur = cur.next
                carry = 0
        
        return self.reverse(dummy.next)
        
        
    def reverse(self, head):
        pre = None
        
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
            
        return pre
