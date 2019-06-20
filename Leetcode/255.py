# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
# T: O(n)
# S: O(n)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        min_val = -sys.maxsize - 1
        for num in preorder:
            if num < min_val:
                return False
            while stack and num > stack[-1]:
                min_val = stack.pop()
            stack.append(num)
        return True