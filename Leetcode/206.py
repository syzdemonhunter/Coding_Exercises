# https://leetcode.com/problems/reverse-linked-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur_node = head
        prev_node = None
        
        while cur_node:
            # Store the next node in a temporary variables
            next_node = cur_node.next
            
            # Reverse the link
            cur_node.next = prev_node
            
            #Update the previous node to the current node
            prev_node = cur_node
            
            # Proceed to the next node in the original linked list
            cur_node = next_node
            
        # Once the linked list has been reversed, prev_node will be
        # referring to the new head. So return it.
        return prev_node
        