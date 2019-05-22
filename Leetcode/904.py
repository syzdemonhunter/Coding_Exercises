# https://leetcode.com/problems/fruit-into-baskets/
# https://www.youtube.com/watch?v=za2YuucS0tw
# T: O(n)
# S: O(n)

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree or len(tree) == 0:
            return 0
        
        max_val = 1
        my_map = {}
        i, j = 0, 0
        while j < len(tree):
            if len(my_map) <= 2:
                my_map[tree[j]] = j
                j += 1
                
            if len(my_map) > 2:
                min_val = len(tree) - 1
                for value in my_map.values():
                    min_val = min(min_val, value)
                    
                i = min_val + 1
                del my_map[tree[min_val]]
                
            max_val = max(max_val, j - i)
            
        return max_val
                
        