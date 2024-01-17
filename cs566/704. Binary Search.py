# https://leetcode.com/problems/binary-search/description/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def next(l, r):
            if l >= r:
                return -1
            mid = (l + r) >> 1
            if nums[mid] > target:
                return next(l, mid)
            elif nums[mid] < target:
                return next(mid + 1, r)
            return mid

        return next(0, len(nums))

