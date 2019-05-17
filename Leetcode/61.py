# https://leetcode.com/problems/rotate-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k <= 0:
            return head
        end = head
        cnt = 1
        while end.next:
            end = end.next
            cnt += 1
        end.next = head
        k %= cnt
        new_end = head
        for i in range(cnt - k - 1):
            new_end = new_end.next
        new_head = new_end.next
        new_end.next = None
        return new_head