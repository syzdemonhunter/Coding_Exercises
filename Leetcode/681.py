# https://leetcode.com/problems/next-closest-time/

#有两种思路可以选择, 一种是从已有数字出发, 另一种是从时间点出发. 由于问题规模很小, 两种方法都可以顺利通过, 几乎没有性能差距.
#注意: 分钟是60进制, 小时是24进制.
#方法1:
#从给定时间点一分钟一分钟地递增, 即枚举每一个时间点, 直到这个时间点可以被给定的数字组成为止.

#方法2:
#用已有的数字生成所有排列, 在这些排列中找到距离原时间点最近的即可.
import datetime

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time)
        while True:
            time =  (datetime.datetime.strptime(time, '%H:%M') + \
                     datetime.timedelta(minutes=1)).strftime('%H:%M')
            if set(time) <= digits:
                return time
        