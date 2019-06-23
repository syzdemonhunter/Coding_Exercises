# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://blog.csdn.net/chen_xinjia/article/details/69258706
# T: O(log(min(m, n)))
# S: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        length = len(nums1) + len(nums2)
        cut1, cut2 = 0, 0
        cutL, cutR = 0, len(nums1)
        while cut1 <= len(nums1):
            cut1 = (cutR - cutL)//2 + cutL
            cut2 = length//2 - cut1
            L1 = -sys.maxsize - 1 if cut1 == 0 else nums1[cut1 - 1]
            L2 = -sys.maxsize - 1 if cut2 == 0 else nums2[cut2 - 1]
            R1 = sys.maxsize if cut1 == len(nums1) else nums1[cut1]
            R2 = sys.maxsize if cut2 == len(nums2) else nums2[cut2]
            
            if L1 > R2:
                cutR = cut1 - 1
            elif L2 > R1:
                cutL = cut1 + 1
            else:
                if length % 2 == 0:
                    L1 = L1 if L1 > L2 else L2
                    R1 = R1 if R1 < R2 else R2
                    return (L1 + R1) / 2
                else:
                    R1 = R1 if R1 < R2 else R2
                    return R1
                
        return -1