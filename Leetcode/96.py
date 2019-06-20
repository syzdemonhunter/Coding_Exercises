# https://leetcode.com/problems/unique-binary-search-trees/
# T: O(n)
# S: O(n)
# f(n) = f(0)*f(n - 1) + f(1)*f(n - 2) + ..... + f(n - 1)*f(0)

class Solution:
    def numTrees(self, n: int) -> int:
        result = [0]*(n + 1)
        result[0] = 1
        for i in range(1, n + 1):
            for j in range(0, i):
                result[i] += result[j]*result[i - j - 1]
                
        return result[n]
        