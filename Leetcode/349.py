# https://leetcode.com/problems/intersection-of-two-arrays/submissions/
# https://www.youtube.com/watch?v=dP8CAXKISX0
# T: O(m + n)
# S: O(m + n)

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1, set2 = set(nums1), set()
        for num2 in nums2:
            if num2 in set1:
                set2.add(num2)
                
        result = [0]*len(set2)
        for i in range(len(list(set2))):
            result[i] = list(set2)[i]
            
        return result