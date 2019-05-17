# https://leetcode.com/problems/lru-cache/

class DoubleNode(object):
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        # contains key and Node memaddr
        self._index = {}
        self._head = DoubleNode(-1, -1, None, None)

        cur = self._head
        for i in range(1, capacity):
            cur.next = DoubleNode(-1, -1, cur)
            cur = cur.next
        cur.next = self._head
        self._head.pre = cur

    def move_to_head(self, cur):
        if cur == self._head:
            self._head = self._head.pre
            return
        # detatch
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        # attach to head pointer
        cur.next = self._head.next
        cur.next.pre = cur
        self._head.next = cur
        cur.pre = self._head
        return

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        cur = self._index.get(key, None)
        if not cur:
            return -1
        else:
            self.move_to_head(cur)
            return cur.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._index.get(key, None):
            cur = self._index[key]
            cur.val = value
            self.move_to_head(cur)
        else:
            if self._head.val != -1:
                del(self._index[self._head.key])
            self._head.key = key
            self._head.val = value
            self._index[key] = self._head
            self._head = self._head.pre


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)