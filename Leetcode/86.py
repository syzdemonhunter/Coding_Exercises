# https://leetcode.com/problems/partition-list/
# T: O(n)
# S: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = ListNode(0)
        big_head = ListNode(0)
        
        small = small_head
        big = big_head
        
        while head:
            tmp = ListNode(head.val)
            if head.val < x:
                small.next = tmp
                small = small.next
            else:
                big.next = tmp
                big = big.next
            head = head.next
            
        small.next = big_head.next
        return small_head.next