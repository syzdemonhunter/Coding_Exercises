# https://leetcode.com/problems/find-k-closest-elements/
# https://www.youtube.com/watch?v=kSxcZdpV2CA
# T: O(n)
# S: O(n)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = self.bin_search(arr, k, x)
        low, high = closest, closest
        while high - low + 1 < k and low > 0 and high <  len(arr) - 1:
            if abs(arr[low - 1] - x) <= abs(arr[high + 1] - x):
                low -= 1
            else:
                high += 1
                
        while high - low + 1 < k:
            if low > 0:
                low -= 1
            else:
                high += 1
                
        result = []
        while low <= high:
            result.append(arr[low])
            low += 1
        return result
    
    def bin_search(self, arr, k, x):
        low, high, min_diff, closest = 0, len(arr) - 1, float('inf'), -1
        while low <= high:
            mid = low + (high - low)//2
            cand = arr[mid]
            if abs(cand - x) < min_diff:
                min_diff = abs(cand - x)
                closest = mid
            if cand == x:
                return mid
            elif cand  < x:
                low = mid + 1
            else:
                high = mid - 1
                
        return closest