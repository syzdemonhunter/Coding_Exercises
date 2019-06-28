# https://leetcode.com/problems/intersection-of-two-arrays-ii/

'''
# T: O(n)
# S: O(n)

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        ret = []
        for i in range(len(nums1)):
            dic[nums1[i]] = dic.get(nums1[i], 0) + 1
            
        for i in range(len(nums2)):
            if nums2[i] in dic:
                if dic[nums2[i]] > 0:
                    ret.append(nums2[i])
                    dic[nums2[i]] -= 1
                    
        result = [0]*len(ret)
        k = 0
        for num in ret:
            result[k] = num
            k += 1
            
        return result
'''
# T: O(nlogn)
# S: O(n)

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        ret = []
        
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ret.append(nums1[i])
                i += 1
                j += 1
                
        result = [0]*len(ret)
        k = 0
        for num in ret:
            result[k] = num
            k += 1
            
        return result
        