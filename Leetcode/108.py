# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left)//2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid - 1)
        node.right = self.helper(nums, mid + 1, right)
        return node
        