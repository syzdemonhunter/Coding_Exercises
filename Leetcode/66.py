# https://leetcode.com/problems/plus-one/discuss/159471/Python-solution
# T: O(n)
# S: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i]+carry, 10)
            if carry == 0:
                return digits
        return [1] + digits
        