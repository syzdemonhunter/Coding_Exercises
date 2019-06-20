# https://leetcode.com/problems/combinations/
# T: O(n^min(k, n - k))
# S: O(n)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.dfs(result, [], n, k, 1)
        return result
        
    def dfs(self, result, path, n, k, start):
        if k == 0:
            result.append(path)
            return
        
        for i in range(start, n + 1):
            self.dfs(result, path + [i], n, k - 1, i + 1)
        