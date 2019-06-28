# https://leetcode.com/problems/intersection-of-two-arrays/

'''
# T: O(nlogn)
# S: O(n)

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or len(nums1) == 0 or \
           not nums2 or len(nums2) == 0:
            return []
        
        my_set = set()
        nums2.sort()
        for num in nums1:
            if self.bin_search(nums2, num):
                my_set.add(num)
                
        k = 0
        result = [0]*len(my_set)
        for num in my_set:
            result[k] = num
            k += 1
            
        return result
                
    def bin_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[start] == target or nums[end] == target:
            return True
        return False
'''
'''
# T: O(nlogn)
# S: O(n)

class Solution(object):
    def intersection(self, nums1, nums2):
        if not nums1 or len(nums1) == 0 or \
           not nums2 or len(nums2) == 0:
            return []
        
        my_set = set()
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                my_set.add(nums1[i])
                i += 1
                j += 1
                
        k = 0
        result = [0]*len(my_set)
        for num in my_set:
            result[k] = num
            k += 1
            
        return result
'''
# T: O(n)
# S: O(n)

class Solution(object):
    def intersection(self, nums1, nums2):
        if not nums1 or len(nums1) == 0 or \
           not nums2 or len(nums2) == 0:
            return []
        
        my_set = set()
        ret = set()
        for num in nums1:
            my_set.add(num)
            
        for num in nums2:
            if num in my_set:
                ret.add(num)
        
        k = 0
        result = [0]*len(ret)
        for num in ret:
            result[k] = num
            k += 1
            
        return result