# https://github.com/syzdemonhunter/Coding_Exercises/blob/master/Leetcode/188.py
# T: O(n)
# S: O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_val = float('inf')
        sec_min_val = float('inf')
        
        for num in nums:
            if num <= min_val:
                min_val = num
            elif num < sec_min_val:
                sec_min_val = num
            elif num > sec_min_val:
                return True
            
        return False

        