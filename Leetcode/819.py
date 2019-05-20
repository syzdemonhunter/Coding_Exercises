# https://leetcode.com/problems/most-common-word/

import re
import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        word_count = collections.Counter(w for w in words if w not in ban)
        return word_count.most_common(1)[0][0]