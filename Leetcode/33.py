# https://algocasts.io/episodes/6emEOjpV
# T: O(log(n))
# S: O(1)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1