# T: O(n^2)
# S: O(1)

def longestPalindromicSubstring(string):
    cur_longest = [0, 1]
    for i in range(1, len(string)):
        odd = helper(string, i - 1, i + 1)
        even = helper(string, i - 1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        cur_longest = max(longest, cur_longest, key = lambda x: x[1]  - x[0])
        
    return string[cur_longest[0]: cur_longest[1]]

def helper(string, left, right):
    while left >= 0  and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
        
    return [left + 1, right]