# https://leetcode.com/problems/maximize-distance-to-closest-person/
# T: O(n)
# S: O(1)

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # left记载当前位置左边第一个1的位置
        # count进行0的计数
        # _max_distance维护最大距离返回值
        left, count, max_distance = -1, 0, 1
        for i, x in enumerate(seats):
            if x == 0:
                count += 1
            else:
                if left < 0:
                    # 左边没有1最大距离就是count
                    distance = count
                else:
                    # 左边有1最大距离就是一半左右
                    # 奇数个0正好在中间
                    # 偶数个0要比一半小1
                    distance = count // 2 + count % 2
                # 重置左边第一个1的位置
                # 遇到1重新计数0的个数
                left, count = i, 0
                # 更新最大距离
                max_distance = max(max_distance, distance)
        # 末尾一连串0的情况也可能刷新最大距离
        return max(max_distance, count)
        
        