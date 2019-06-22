# https://leetcode.com/problems/reverse-nodes-in-k-group/
# T: O(n)
# S: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        count = 0
        cur = head
        while cur and count != k:
            cur = cur.next
            count += 1
        
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
            
        return head