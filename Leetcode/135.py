# https://leetcode.com/problems/candy/
# T: O(n)
# S: O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        
        for i in range(1, len(candies)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        for i in range(len(candies) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        result = 0
        for candy in candies:
            result += candy
            
        return result