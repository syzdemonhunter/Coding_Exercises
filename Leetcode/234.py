# https://leetcode.com/problems/palindrome-linked-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        middle = self.find_mid(head)
        middle.next = self.reverse(middle.next)
        
        p = head
        q = middle.next
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True
        
        
    def find_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def reverse(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev= head
            head = tmp
            
        return prev
        
        
        