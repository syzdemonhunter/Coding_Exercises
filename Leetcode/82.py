# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                same_num = p.next.val
                while p.next and p.next.val == same_num:
                    p.next = p.next.next
                    
            else:
                p = p.next
                
        return dummy.next
        