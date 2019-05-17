# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = pre.next
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next != cur:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = pre.next
        return dummy.next