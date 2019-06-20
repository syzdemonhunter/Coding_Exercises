# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 面试中没怎么太考，基础题
# T: O(n)
# S: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) < 2:
            return [-1, -1]
        
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if target == total:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
                
        return [-1, -1]
        