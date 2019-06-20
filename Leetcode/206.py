# https://leetcode.com/problems/reverse-linked-list/
# T: O(n)
# S: O(1)
# 闭着眼睛都要能写出来

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
            
        return pre
            