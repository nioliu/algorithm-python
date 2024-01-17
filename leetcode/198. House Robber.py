# https://leetcode.com/problems/house-robber/description/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def grabNext(curr_house) -> int:
            """
            return the sub max arr
            """
            if curr_house >= len(nums):
                return 0
            if dp[curr_house] != -1:
                return dp[curr_house]
            # rob current or not
            curr_res = max(
                nums[curr_house] + grabNext(curr_house + 2),
                grabNext(curr_house + 1)
            )
            dp[curr_house] = curr_res

            return curr_res

        return grabNext(0)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
