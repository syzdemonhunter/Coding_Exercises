# https://leetcode.com/problems/majority-element-ii/
# I keep up to two candidates in my counter, so this fulfills the O(N) time and O(1) space requirements.
#  Collect (count) the votes for every number, but remove triples of three different votes on the fly, as soon as we have such a triple.
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1, e2, cnt1, cnt2 = 0, 0, 0, 0
        
        for num in nums:
            if cnt1 == 0 and num != e2:
                e1 = num
            if num == e1:
                cnt1 += 1
            elif num != e1:
                if cnt2 == 0:
                    e2 = num
                if num == e2:
                    cnt2 += 1
                elif num != e2:
                    cnt1 -= 1
                    cnt2 -= 1
                    
        result = []
        if cnt1 > 0 and nums.count(e1) > len(nums) // 3:
            result.append(e1)
        if cnt2 > 0 and nums.count(e2) > len(nums) // 3:
            result.append(e2)
        return result