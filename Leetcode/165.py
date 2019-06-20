# https://leetcode.com/problems/compare-version-numbers/
# 面试里考的次数不多
# T: O(n)
# S: O(n)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        
        for i in range(max(len(v1_list), len(v2_list))):
            num1 = int(v1_list[i]) if i < len(v1_list) else 0
            num2 = int(v2_list[i]) if i < len(v2_list) else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0
        