# https://leetcode.com/problems/add-two-numbers/
# T: T: O(max(m, n)) m, n: lengh of l1, l2
# S: T: O(max(m, n))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        p = dummy
        while p1 or p2 or carry:
            total = carry
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next
            p.next = ListNode(total%10)
            p = p.next
            carry = total//10
        return dummy.next