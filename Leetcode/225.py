# https://leetcode.com/problems/implement-stack-using-queues/

import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for i in range(len(self.q)):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()