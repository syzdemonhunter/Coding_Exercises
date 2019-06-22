# https://leetcode.com/problems/merge-k-sorted-lists/
# 建议用heap做这个题
# T: O(nlogk)
# S: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        
        min_heap = []
        dummy = ListNode(0)
        cur = dummy
        
        min_heap = []
        for lst in lists:
            while lst:
                heapq.heappush(min_heap, lst.val)
                lst = lst.next
        
        while min_heap:
            cur.next = ListNode(heapq.heappop(min_heap))
            cur = cur.next
            
        return dummy.next