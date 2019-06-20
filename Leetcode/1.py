# https://leetcode.com/problems/two-sum/
# T: O(n)
# S: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return [-1, -1]
        result = [-1, -1]
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                result[0] = dic[target - nums[i]]
                result[1] = i
                break
                
            dic[nums[i]] = i
            
        return result
        
            
        