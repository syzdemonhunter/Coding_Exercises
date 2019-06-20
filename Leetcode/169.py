# https://leetcode.com/problems/majority-element/submissions/
'''
# T: O(n)
# S: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                result = num
                break
        return result
'''
# T: O(n)
# S: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for num in nums:
            if count == 0:
                result = num
            if num != result:
                count -= 1
            else:
                count += 1
        return result
        

        
        