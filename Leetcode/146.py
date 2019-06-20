# https://leetcode.com/problems/lru-cache/
# https://algocasts.io/episodes/rLmP8moY
# T: O(1)
# 太难了

class DoubleNode:
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.index = {}
        self.head = DoubleNode(-1, -1, None, None)

        cur = self.head
        for i in range(1, capacity):
            cur.next = DoubleNode(-1, -1, cur)
            cur = cur.next
        cur.next = self.head
        self.head.pre = cur
        
    def move_to_head(self, cur):
        if cur == self.head:
            self.head = self.head.pre
            return
        # detatch
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        # attach to head pointer
        cur.next = self.head.next
        cur.next.pre = cur
        self.head.next = cur
        cur.pre = self.head
        return
        

    def get(self, key: int) -> int:
        cur = self.index.get(key, None)
        if not cur:
            return -1
        else:
            self.move_to_head(cur)
            return cur.val
        

    def put(self, key: int, value: int) -> None:
        if self.index.get(key, None):
            cur = self.index[key]
            cur.val = value
            self.move_to_head(cur)
        else:
            if self.head.val != -1:
                del(self.index[self.head.key])
            self.head.key = key
            self.head.val = value
            self.index[key] = self.head
            self.head = self.head.pre
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)