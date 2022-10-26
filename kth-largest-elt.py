from __future__ import annotations

import heapq
from typing import *


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums = [-1 * x for x in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return heapq.heappop(nums) * -1


class EffSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lnums = len(nums)
        if lnums == 1:
            return nums[0]

        p = nums[lnums // 2]
        lt = []
        ge = []

        for i, x in enumerate(nums):
            if i != lnums // 2:
                if x < p:
                    lt.append(x)
                else:
                    ge.append(x)

        if len(ge) == k - 1:  # p
            return p
        elif len(ge) >= k - 1:  # lt
            return self.findKthLargest(ge, k)
        else:  # ge
            return self.findKthLargest(lt, k - len(ge) - 1)


EffSolution().findKthLargest([3,2,1,5,6,4],2)