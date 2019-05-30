# https://leetcode.com/problems/asteroid-collision/
# 最后的答案序列或者是全正, 或者是全负, 或者是左负右正.

# 借用栈遍历一次数组就可以判断出哪些行星会因碰撞而爆炸:

# 碰到正数直接入栈
# 碰到负数, 不断将它与栈顶比较, 弹出栈顶直至栈顶为负或者栈为空或者栈顶绝对值不小于当前的数.
# 如果栈为空或栈顶为负数, 入栈 (此时栈内的负数一定就是最后会保留下来的向左移动的行星)
# 如果栈顶为正且绝对值大于当前的数, 不再做任何操作
# 如果栈顶为正且绝对值等于当前的数, 将栈顶弹出
# 这样遍历一次之后, 从栈底到栈顶就是答案序列.
# T: O(n)
# S: O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        i, n = 0, len(asteroids)
        while i < n:
            if asteroids[i] > 0:
                result.append(asteroids[i])
            elif len(result) == 0 or result[-1] < 0:
                result.append(asteroids[i])
            elif result[-1] <= -asteroids[i]:
                if result[-1] < -asteroids[i]:
                    i -= 1
                result.pop()
            i += 1
            
        return result