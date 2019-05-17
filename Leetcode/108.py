# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# T: O(n)
# S: O(log(n))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, nums, start, end):
        if start > end:
            return None
        mid = start + (end - start)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, start, mid - 1)
        root.right = self.helper(nums, mid + 1, end)
        return root
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.helper(nums, 0, len(nums) - 1)