from typing import *
from bisect import bisect_left
from heapq import *
import functools

# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         data = sorted(zip(startTime, endTime, profit), key=lambda x : x[1])
#         dp = [[0,0]]
#         for s,e,p in data:
#             idx = bisect_left(dp, [s+1]) - 1
#             if dp[idx][1] + p > dp[-1][1]:
#                 dp.append([e,dp[idx][1] + p])
#         return dp[-1][1]
    
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        hp = []
        total = 0

        for s,e,p in jobs:
            print((s,e,p), hp)
            while hp and hp[0][0] <= s:
                popd = heappop(hp)
                total = max(total, popd[1])
                print((s,e,p), hp)

            heappush(hp, (e, p + total))

        while hp:
            print((s,e,p), hp)
            popd = heappop(hp)
            total = max(total, popd[1])

        return total

@functools.cache
def fib(n):
    if n <= 2:
        return n
    return fib(n-1) + fib(n-2)

print(Solution().jobScheduling([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60]))