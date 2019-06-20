# https://leetcode.com/problems/read-n-characters-given-read4/
# T: O(n)
# S: O(1)

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

'''
The meaning here is that read4() function will read 4 characters at a time from a file and then put the characters that has been read into this buf variable.
So read() function is reading at most n characters from a file ( we don’t know what file and how it’s reading from the file), and put x characters into char[] buf.
'''

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tmp = ['']*4
        idx = 0
        while True:
            count = read4(tmp)
            count = min(count, n - idx)
            for i in range(count):
                buf[idx] = tmp[i]
                idx += 1
            if idx == n or count < 4:
                return idx
                
    
        