# https://leetcode.com/problems/strobogrammatic-number-ii/
# T: O(n^2)
# S: O(1)

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.helper(n, n)
    
    def helper(self, n, m):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        path = self.helper(n - 2, m)
        result = []
        for i in range(len(path)):
            s = path[i]
            if n != m:
                result.append('0' + s + '0')
            result.append('1' + s + '1')
            result.append('6' + s + '9')
            result.append('8' + s + '8')
            result.append('9' + s + '6')
        return result
                