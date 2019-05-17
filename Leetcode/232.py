#https://leetcode.com/problems/implement-queue-using-stacks/submissions/

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack, self.out_stack = [], []
        
    # O(1)
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)
        
    def transfer_is_empty(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
    # O(n)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.transfer_is_empty()
        return self.out_stack.pop()
    
    # O(1)
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.out_stack:
            return self.out_stack[-1]
        else:
            return self.in_stack[0]
        
    # O(1)    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()