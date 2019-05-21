# https://leetcode.com/problems/reorder-list/
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
        if not head:
            return head
        low = fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        tmp = low.next
        low.next = None
        
        # reverse the right half
        tail = cur = tmp
        while cur and cur.next:
            cur = cur.next
            tail.next = cur.next
            cur.next = tmp
            tmp = cur
            cur = tail
            
        # insert in order
        mid = tmp
        while mid:
            tmp = mid.next
            mid.next = head.next
            head.next = mid
            head = head.next.next
            mid = tmp
        