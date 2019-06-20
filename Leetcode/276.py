# https://leetcode.com/problems/paint-fence/
# T: O(n)
# S: O(1)

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same, diff, total = 0, k, k
        for i in range(2, n + 1):
            same = diff
            diff = (k - 1)*total
            total = same + diff
            
        return total
            
        