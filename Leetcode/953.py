# https://leetcode.com/problems/verifying-an-alien-dictionary/

# Build a transform mapping from order,
# Find all alien words with letters in normal order.
# For example, if we have order = "xyz..."
# We can map the word "xyz" to "abc" or "123"
# Then we check if all words are in sorted order.
# Time complexity： O(NS)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            for c1, c2 in zip(w1, w2):
                if order_map[c1] > order_map[c2]:
                    return False
                elif  order_map[c1] < order_map[c2]:
                    break
                    
        return True
        
        