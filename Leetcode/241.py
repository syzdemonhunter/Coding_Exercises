# https://leetcode.com/problems/different-ways-to-add-parentheses/
# T: O(n^3) ???
# S: O(n)

class Solution:
    def diffWaysToCompute(self, input_nums: str) -> List[int]:
        result = []
        for i in range(len(input_nums)):
            c = input_nums[i]
            if c == '-' or c == '+' or c == '*':
                a = input_nums[:i]
                b = input_nums[i + 1:]
                al = self.diffWaysToCompute(a)
                bl = self.diffWaysToCompute(b)
                for x in al:
                    for y in bl:
                        if c == '-':
                            result.append(x - y)
                        elif c == '+':
                            result.append(x + y)
                        elif c == '*':
                            result.append(x*y)
                            
        if len(result) == 0:
            result.append(int(input_nums))
            
        return result
        