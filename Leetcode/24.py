# https://leetcode.com/problems/swap-nodes-in-pairs/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        l1 = dummy
        l2 = head
        while l2 and l2.next:
            next_start = l2.next.next
            l1.next = l2.next
            l2.next.next = l2
            l2.next = next_start
            l1 = l2
            l2 = l2.next

        return dummy.next
        