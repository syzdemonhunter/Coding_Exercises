# https://leetcode.com/problems/palindrome-linked-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        pre = None
        
        while cur != None:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
            
        return pre
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        slow = self.reverseList(slow)
        fast = head
        
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
            
        return True