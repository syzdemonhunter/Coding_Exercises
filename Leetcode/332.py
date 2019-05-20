# https://leetcode.com/problems/reconstruct-itinerary/
# T: O(n) + O(nlogn) + O(n!)
# S: O(n)

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = collections.defaultdict(list)
        for tkt_0, tkt_1 in sorted(tickets)[::-1]:
            d[tkt_0] += tkt_1,
            
        result = []
        self.dfs(d, 'JFK', result)
        return result[::-1]
    
    def dfs(self, d, airport, result):
        while d[airport]:
            self.dfs(d, d[airport].pop(), result)
        result.append(airport)
