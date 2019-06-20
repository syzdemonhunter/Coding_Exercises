# https://leetcode.com/problems/two-sum-iii-data-structure-design/

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    # time: O(1)
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.dic[number] = self.dic.get(number, 0) + 1
        
    # time: O(n)
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.dic.keys():
            j = value - i
            if (i == j and self.dic.get(i) > 1) or (i != j and j in self.dic):
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)