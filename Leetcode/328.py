# https://leetcode.com/problems/odd-even-linked-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        even_dummy_head = ListNode(0)
        odd_dummy_head = ListNode(0)
        
        tails, turn = [even_dummy_head, odd_dummy_head], 0
        
        while head:
            tails[turn].next = head
            head = head.next
            tails[turn] = tails[turn].next
            turn ^= 1
            
        tails[1].next = None
        tails[0].next = odd_dummy_head.next
        return even_dummy_head.next