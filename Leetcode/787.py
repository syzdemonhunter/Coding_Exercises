# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# https://www.jiuzhang.com/solution/cheapest-flights-within-k-stops/#tag-highlight-lang-java
# Time complexity: O(k * |flights|) / O(k*n^2)
# Space complexity: O(k*n) -> O(n)
# w/o space compression O(k*n)

# 该题目是一道加了限制的最短路题目, 即限制最多有 K + 1 条边构成.
# 在Bellman-Ford或者Dijkstra最短路算法的基础上做一点修改即可.
# 如果是Bellman-Ford(或者是由该算法优化而来的SPFA算法), 那么需要限制迭代次数, 最多 K + 1 条边, 只迭代 K + 1 次即可.
# 同时还需要保证每一次迭代只会让边生长一次. (Bellman-Ford需要记录并判断, 而SPFA无需关注这一点)
# 如果是Dijkstra算法, 则需要额外记录一下当前点距离源点的边数.
# 该问题数据范围不大, 同时提供的是所有的边的集合, 所以很适合使用Bellman-Ford算法.


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        distance = [sys.maxsize for i in range(n)]
        distance[src] = 0
        
        for i in range(K + 1):
            dN = list(distance)    	# 直接把最短路数组复制一遍, 用副本保存松弛的结果, 也可以保证每一轮迭代最多增加一条边, 不过执行效率略低
            for u, v, c in flights:
                dN[v]= min(dN[v], distance[u] + c)
            distance = dN
            
        if distance[dst] != sys.maxsize:
            return distance[dst]
        else:
            return -1