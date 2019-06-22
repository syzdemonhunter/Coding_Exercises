# https://leetcode.com/problems/bulb-switcher/
# T: O(1)
# S: O(1)

import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))