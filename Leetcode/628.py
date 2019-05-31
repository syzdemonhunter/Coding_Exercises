# https://leetcode.com/problems/maximum-product-of-three-numbers/
# O(n) time and O(1) additional space.
# Simply find out the three largest numbers and the two smallest numbers using one pass.

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return
        
        max1, max2, max3 = -float('inf'), -float('inf'), -float('inf')
        min1, min2 = float('inf'), float('inf')
        
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
                
            elif num > max2:
                max3 = max2
                max2 = num
                
            elif num > max3:
                max3 = num
                
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            
        return max(max1*max2*max3, max1*min1*min2)
            