# https://leetcode.com/problems/meeting-rooms-ii/
# https://www.youtube.com/watch?v=PWgFnSygweI
# T: O(n)
# S: O(nlogn)

#We need a data structure that dynamically keeps track of the meeting end times and fast access aka O(1) to the smallest end time.
#A heap is an option.
#The heap stores the smallest end time at the top.
#First, we need to sort the input.
#When we update the heap with a new meeting, we check if its start time is before the current smallest end time.
#If yes, we add the meeting to the heap. This mean we need an additional room.
#Otherwise, the first meeting ended and can be removed from the heap. We add the new meeting to the heap.
#Eventually, the heap stores all the meetings that need separate rooms.

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda a: a[0])
        min_heap = []
        
        heapq.heappush(min_heap, (intervals[0][1], intervals[0]))
        
        for i, interval in enumerate(intervals):
            if i != 0:
                start, end = interval[0], interval[1]
                if start >= min_heap[0][1][1]:
                    heapq.heappop(min_heap)
                    
                heapq.heappush(min_heap, (interval[1], interval))
                
        return len(min_heap)
        
        