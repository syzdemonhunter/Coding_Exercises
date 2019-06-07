# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# https://www.youtube.com/watch?v=H8hoDlakuK4
# T: O(nlogn)
# S: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        def findMin(head):
            slow = fast = head
            prev = None
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow
                
        mid = findMin(head)
        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head) # 从head到mid - 1
        root.right = self.sortedListToBST(mid.next) # 从mid + 1 到 Tail

        return root