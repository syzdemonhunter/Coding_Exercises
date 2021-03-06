# https://leetcode.com/problems/design-phone-directory/

import collections

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.used = set()
        self.q = collections.deque()
        self.maxNumbers = maxNumbers
        for i in range(self.maxNumbers):
            self.q.append(i)

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if not self.q:
            return -1
        result = self.q.popleft()
        self.used.add(result)
        return result
        

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        if number >= self.maxNumbers or number < 0:
            return False
        return number not in self.used

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.used:
            self.used.remove(number)
            self.q.append(number)
            
        
            


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)