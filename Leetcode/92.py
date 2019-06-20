# https://leetcode.com/problems/reverse-linked-list-ii/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        
        for i in range(1, m):
            cur = cur.next
            pre = pre.next
            
        for i in range(0, n - m):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
            
        return dummy.next
        