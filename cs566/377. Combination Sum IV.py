# https://leetcode.com/problems/combination-sum-iv/?envType=daily-question&envId=2023-10-05
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0

            count = 0
            for num in nums:
                if n - num < 0:
                    break
                count += helper(n - num)

            memo[n] = count
            return count

        return helper(target)


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
