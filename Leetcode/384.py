# https://leetcode.com/problems/shuffle-an-array/
# T: O(n)
# S: O(1)

class Solution:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.origin = nums[:]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        length = len(self.data) - 1
        for i in range(length, 0, -1):
            j = random.randrange(0, i + 1)
            self.data[j], self.data[i] = self.data[i], self.data[j]
            
        return self.data

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()