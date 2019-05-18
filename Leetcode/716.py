# https://leetcode.com/problems/max-stack/
# T: O(n)
# S: O(n)

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.max_s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if not self.max_s:
            self.max_s.append(x)
        else:
            self.max_s.append(max(x, self.max_s[-1]))

    def pop(self):
        """
        :rtype: int
        """
        self.max_s.pop()
        return self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max_s[-1]
        

    def popMax(self):
        """
        :rtype: int
        """
        p = self.max_s.pop()
        tmp_list = []
        
        while p != self.s[-1]:
            tmp_list.append(self.pop())
        result = self.s.pop()
        
        for i in range(len(tmp_list) - 1, -1, -1):
            self.push(tmp_list[i])
            
        return result
            
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()