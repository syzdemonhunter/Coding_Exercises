# https://leetcode.com/problems/combination-sum-iii/
# T: O(2^n)
# S: O(n)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.dfs(result, [], k, n, 1)
        return result
    
    def dfs(self, result, path, k, n, start):
        if k == 0 and n == 0:
            result.append(path)
            return
        for i in range(start, 10):
            self.dfs(result, path + [i], k - 1, n - i, i + 1)
            