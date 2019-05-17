# https://leetcode.com/problems/reverse-linked-list/
# T: O(n)
# S: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        pre = None
        while cur is not None:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        return pre
