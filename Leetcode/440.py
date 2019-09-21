# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# T: O((logk ~ k)logn)
# S: O(1)

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        result = 1
        k -= 1
        while k > 0:
            steps = 0
            first = result
            last = result + 1
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
                
            if steps <= k:
                result += 1
                k -= steps
            else:
                result *= 10
                k -= 1
                
        return result