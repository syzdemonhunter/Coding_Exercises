# https://leetcode.com/problems/unique-binary-search-trees-ii/
# https://www.youtube.com/watch?v=GZ0qvkTAjmw
# time 应该是N^3 space应该 是o(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(1, n)
    
    def helper(self, min_val, max_val):
        if min_val > max_val:
            return []
        
        result = []
        for rt in range(min_val, max_val + 1):
            left_list = self.helper(min_val, rt - 1)
            right_list = self.helper(rt + 1, max_val)
            if len(left_list) == 0 and len(right_list) == 0:
                root = TreeNode(rt)
                result.append(root)
                
            elif len(left_list) == 0:
                for right in right_list:
                    root = TreeNode(rt)
                    root.right = right
                    result.append(root)
                    
            elif len(right_list) == 0:
                for left in left_list:
                    root = TreeNode(rt)
                    root.left = left
                    result.append(root)
            else:
                for left in left_list:
                    for right in right_list:
                        root = TreeNode(rt)
                        root.left = left
                        root.right = right
                        result.append(root)
                        
        return result
        
        