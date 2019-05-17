# https://leetcode.com/problems/insert-delete-getrandom-o1/
# https://www.jiuzhang.com/solution/657-insert-delete-getrandom-o-1/#tag-highlight-lang-python
# 如果仅实现insert/remove的话，那么可以直接用哈希表解决。
# 使用（动态）数组(vector in C++, list in Python and ArrayList in Java)可以很方便地实现getRandom操作，只要先随机取一个下标，然后返回该下标对应的元素即可。
# 因此考虑将这两种数据结构结合起来，用一个哈希表和一个数组来维护集合中的元素。

# insert:可以直接在数组后面添加一个新元素，并在哈希表中记录下该元素对应的数组下标。
# remove:先将待删除的元素与数组中最后一个元素调换，由于两个元素的顺序调换了，它们在哈希表中记录的下标也应该调换。调换完成后，待删除元素变成了数组中最后一个元素，故直接将数组长度减一并将该元素从哈希表中移除即可。
# getRandom: 直接随机取一个下标然后返回该下标对应的元素即可。

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_list = []
        self.nums_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums_map:
            return False
        
        self.nums_map[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
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

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()