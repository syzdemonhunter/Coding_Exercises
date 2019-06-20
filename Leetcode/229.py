# https://leetcode.com/problems/majority-element-ii/
# Moore voting algorithm
# 每次都找出一对不同的元素， 从数组中删掉，直到数组为空或只有一种元素
# 不难证明，如果存在元素e出现频率超过半数，那么数组中嘴周剩下的就只有e。
# T: O(n)
# S: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        
        result = []
        num1, num2 = 0, 0
        cnt1, cnt2 = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == num1:
                cnt1 += 1
            elif nums[i] == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0:
                num2 = nums[i]
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        cnt1 = cnt2 = 0
        for i in range(len(nums)):
            if nums[i] == num1:
                cnt1 += 1
            elif nums[i] == num2:
                cnt2 += 1
                
        if cnt1 > len(nums)//3:
            result.append(num1)
            
        if cnt2 > len(nums)//3:
            result.append(num2)
            
        return result
            
        
                
            
        