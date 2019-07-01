# https://leetcode.com/problems/insert-delete-getrandom-o1/
# T: O(n)

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_list = []
        self.nums_map = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.nums_map:
            return False
        
        self.nums_map[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.nums_map:
            return False
        
        index = self.nums_map[val]
        last = len(self.nums_list) - 1
        
        self.nums_map[self.nums_list[last]] = index
        self.nums_list[index], self.nums_list[last] =\
        self.nums_list[last], self.nums_list[index]
        
        self.nums_list.pop()
        del self.nums_map[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()