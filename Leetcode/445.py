# https://leetcode.com/problems/add-two-numbers-ii/
# T: O(n)
# S: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = self.list_to_stack(l1), self.list_to_stack(l2)
        sum_val, result = 0, ListNode(0)
        while s1 or s2:
            if s1:
                sum_val += s1.pop()
            if s2: 
                sum_val += s2.pop()
            sum_val, result.val = divmod(sum_val, 10)
            head = ListNode(sum_val)
            head.next = result
            result = head
        if result.val:
            return result
        else:
            return result.next
        
    def list_to_stack(self, node):
        s = []
        while node:
            s.append(node.val)
            node = node.next
        return s