# https://leetcode.com/problems/factor-combinations/

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        self.dfs(result, [], n, 2)
        return result
    
    def dfs(self, result, path, n, start):
        if n == 1:
            if len(path) > 1:
                result.append(path)
                return
        for i in range(start, n + 1):
            if n % i == 0:
                self.dfs(result, path + [i], n//i, i)
        