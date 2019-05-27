# https://leetcode.com/problems/flatten-2d-vector/
# https://www.jiuzhang.com/solution/flatten-2d-vector/

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.vec_2d = v
        self.row, self.col = 0, -1
        self.next_elem = None
        

    def next(self) -> int:
        if self.next_elem is None:
            self.hasNext()
        
        tmp, self.next_elem = self.next_elem, None
        return tmp
        
    def hasNext(self) -> bool:
        if self.next_elem:
            return True
        self.col += 1
        while self.row < len(self.vec_2d) and self.col >= len(self.vec_2d[self.row]):
            self.row += 1
            self.col = 0
        
        if self.row < len(self.vec_2d) and self.col < len(self.vec_2d[self.row]):
            self.next_elem = self.vec_2d[self.row][self.col]
            return True
        
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()