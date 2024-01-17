# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left = nums[0] - 1
        at = 1
        while left >= 0 and at < len(nums):
            if left < nums[at]:
                left = nums[at]
            if left == 0:
                return False
            at += 1
            left -= 1
        return True


if __name__ == '__main__':
    # s = Solution()
    # print(s.canJump([3, 2, 1, 0, 4]))
    o = [[0] * 3 for _ in range(3)]
    print(id(o[0]), id(o[1]))
    o[0][0] = 1
    print(o)
