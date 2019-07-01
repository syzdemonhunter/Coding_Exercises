# https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        rnode = None
        count = 1
        root = self.head
        
        while root:
            if random.randint(1, count) == 1:
                rnode = root
            root = root.next
            count += 1
        return rnode.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()