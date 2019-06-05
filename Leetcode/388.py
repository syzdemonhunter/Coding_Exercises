# https://leetcode.com/problems/longest-absolute-file-path/
# T: O(n)
# S: O(1)

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dic = {}
        longest = 0
        file_list = input.split('\n')
        for f in file_list:
            if '.' not in f: # 是文件夹
                key = f.count('\t')  #是几级文件夹
                value = len(f.replace('\t', '')) #除去\t后的长度，是实际长度
                dic[key] = value
            else: #是文件。
                key = f.count('\t')
                #　文件的长度：所有目录的长度＋文件的长度＋“\”的数量
                length = sum([dic[j] for j in dic.keys() if j < key]) + len(f.replace("\t","")) + key
                longest = max(longest, length)
                
        return longest
        