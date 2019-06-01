# https://leetcode.com/problems/squares-of-a-sorted-array/
# T: O(n)
# S: O(n)

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer
        