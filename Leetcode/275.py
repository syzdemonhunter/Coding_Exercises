# https://leetcode.com/problems/h-index-ii/
# T: O(logn)
# S: O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations) 
        start, end = 0, length  - 1
        while start <= end:
            mid = start + (end - start)//2
            if citations[mid] == length  - mid:
                return length  - mid
            elif citations[mid] < length - mid:
                start = mid + 1
            else:
                end = mid - 1
                
        return length - start
        