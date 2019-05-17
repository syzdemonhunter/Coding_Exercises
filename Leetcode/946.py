# https://leetcode.com/problems/validate-stack-sequences/
# T: O(n)
# S: O(n)


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pop_idx = 0
        
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
                
        if len(stack) == 0:
            return True
        else:
            return False
        