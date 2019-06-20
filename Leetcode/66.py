# https://leetcode.com/problems/plus-one/
# T: O(n)
# S: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits or len(digits) == 0:
            return digits
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            else:
                digits[i] = 0
                
        return [1] + [0]*len(digits) 
        