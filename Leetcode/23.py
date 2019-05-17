# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time O(n*log(k))
# space O(k)
# n = max # of lists
# m = max # of nodes in a list
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
        
        min_heap = []
        for head in lists:
            while head:
                heapq.heappush(min_heap, head.val)
                head = head.next
                
        dummy = ListNode(0)
        p = dummy
        
        while min_heap:
            p.next = ListNode(heapq.heappop(min_heap))
            p = p.next
            
        return dummy.next
            
                