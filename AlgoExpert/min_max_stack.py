class MinMaxStack:
    def __init__(self):
        self.min_max_stack = []
        self.stack = []
    
    # O(1) T; O(1) S
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    # O(1) T; O(1) S
    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    # O(1) T; O(1) S
    def push(self, number):
        new_min_max = {'min_val': number, 'max_val': number}
        if len(self.min_max_stack):
            last_min_max = self.min_max_stack[len(self.min_max_stack) - 1]
            new_min_max['min_val'] = min(last_min_max['min_val'], number)
            new_min_max['max_val'] = max(last_min_max['max_val'], number)
        self.min_max_stack.append(new_min_max)
        self.stack.append(number)
    
    # O(1) T; O(1) S
    def getMin(self):
        return self.min_max_stack[len(self.min_max_stack) -1]['min_val']

    # O(1) T; O(1) S
    def getMax(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]['max_val']
        
