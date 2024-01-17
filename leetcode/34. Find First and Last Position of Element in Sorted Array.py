# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=daily-question&envId=2023-10-09
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def next(l, r):
            if l >= r:
                return [-1, -1]
            mid = (l + r) >> 1
            if nums[mid] < target:
                return next(mid + 1, r)
            elif nums[mid] > target:
                return next(l, mid)
            else:
                i, j = mid - 1, mid + 1
                while (i >= 0 and nums[i] == target) or (j < len(nums) and nums[j] == target):
                    if i >= 0 and nums[i] == target:
                        i -= 1
                    if j < len(nums) and nums[j] == target:
                        j += 1
                return [i + 1, j - 1]

        return next(0, len(nums))


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 6, 6, 8, 8, 10], 8))
    print(s.searchRange([1, 2, 3], 3))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
