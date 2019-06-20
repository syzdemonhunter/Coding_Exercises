# https://leetcode.com/problems/insertion-sort-list/
# T: O(n^2)
# S: O(1)
# 面试基本不考

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        tmp = None
        pre = None
        
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = tmp.next
                prev = dummy
                while prev.next.val <= tmp.val:
                    prev = prev.next
                tmp.next = prev.next
                prev.next = tmp
        return dummy.next
        
        
        
        