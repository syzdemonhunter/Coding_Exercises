# https://leetcode.com/problems/arithmetic-slices/
# T: O(n)
# S: O(1)

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        cur, result = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cur += 1
                result += cur 
            else:
                cur = 0

        return result
        