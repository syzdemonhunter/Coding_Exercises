# https://leetcode.com/problems/palindrome-permutation/
'''
# T: O(n)
# S: O(n)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        my_set = set()
        for c in s:
            if c in my_set:
                my_set.remove(c)
            else:
                my_set.add(c)
        return len(my_set) <= 1
'''
# T: O(n)
# S: O(1)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = [0]*256
        result = 0
        
        for c in s:
            idx = ord(c) - ord('a')
            if cnt[idx] > 0:
                cnt[idx] -= 1
            else:
                cnt[idx] += 1
                
        for i in range(len(cnt)):
            if cnt[i] != 0:
                result += 1
        return result <= 1
                
        
        