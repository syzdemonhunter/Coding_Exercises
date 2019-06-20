# https://leetcode.com/problems/gray-code/
# G(i) = i^(i/2)
# 这题不用看
# T: O(1 << n) / O(n)
# S: O(1 << n) / O(n)

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(1 << n):
            result.append(i^i >> 1)
        return result
        