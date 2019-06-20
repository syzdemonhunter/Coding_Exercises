# https://leetcode.com/problems/super-ugly-number/
# T: O(nlogk)
# S: O(max(n, k))

# 使用小根堆, 初始将1放入堆, 循环 n-1 次, 每次取出堆顶, 然后将该值与素数列表每个数的乘积再次放入堆.
# 注意可能会有数重复入堆, 所以还需要额外的数据结构记录一个数是否出现过, 把重复的数排除, 以保证取出的堆顶是从小到大的超级丑数.
# n-1 次循环之后, 此时的堆顶即是第 n 个丑数.
# 时间复杂度 O(nklogn)


import heapq
class Solution:
    
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        length = len(primes)
        times = [0]*length
        uglys = [1]
        min_heap = [(primes[i]*uglys[times[i]], i) for i in range(len(times))]
        heapq.heapify(min_heap)

        while len(uglys) < n:
            umin, min_times = heapq.heappop(min_heap)
            times[min_times] += 1
            if umin != uglys[-1]:
                uglys.append(umin)
            heapq.heappush(min_heap, (primes[min_times]*uglys[times[min_times]], min_times))

        return uglys[-1]
        
        