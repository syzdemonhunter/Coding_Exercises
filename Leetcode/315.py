# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# T: O(n^2)
# S: O(n)

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        seen, result = [], []
		# iterate backwards
        for i in range(len(nums) - 1, -1, -1):
			# binary insert to keep sorted order
            bisect.insort(seen, nums[i]) # binary insert to keep sorted order 
			# get index of where nums[i] 
			# would be inserted in the LEFT position
            pos = bisect.bisect_left(seen, nums[i])
            result.append(pos)
        
        return result[::-1]
            
        