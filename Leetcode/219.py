# https://leetcode.com/problems/contains-duplicate-ii/submissions/
# T: O(n)
# S: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if (i - dic[nums[i]]) <= k:
                    return True
            dic[nums[i]] = i
            
        return False