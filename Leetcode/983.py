# https://leetcode.com/problems/minimum-cost-for-tickets/
# T: O(n)
# S: O(n)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_dict = set(days)
        
        # Create a table of all the day cost
        # * Instead of creating a 365 days table, we create until the last day on the days list
        table = [0 for i in range(0, days[-1]+1)]
        
        for i in range(0, days[-1] + 1):
            # If the current day is not present in the travel days dictionary, it takes the previous value
            if i not in days_dict:
                table[i] = table[i-1]
            else:
                # Used max to identify if the index exists 
                table[i] = min(
                    table[max(0,i - 1)] + costs[0], # per days value
                    table[max(0,i - 7)] + costs[1], # per week value
                    table[max(0,i - 30)] + costs[2] # per year value
                )
        return table[-1]