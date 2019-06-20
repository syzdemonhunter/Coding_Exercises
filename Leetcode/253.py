# https://leetcode.com/problems/meeting-rooms-ii/submissions/
# 这题非常非常的重要！！
'''
# T: O(nlogn)
# S: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        
        starts = [0]*len(intervals)
        ends = [0]*len(intervals)
        
        for i in range(len(intervals)):
            starts[i] = intervals[i][0]
            ends[i] = intervals[i][1]
        
        starts.sort()
        ends.sort()
        result = 0
        end = 0
        
        for i in range(len(intervals)):
            if starts[i] < ends[end]:
                result += 1
            else:
                end += 1
                
        return result
'''
# T: O(nlogn)
# S: O(n)

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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
        