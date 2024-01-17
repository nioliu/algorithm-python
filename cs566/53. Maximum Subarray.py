# https://leetcode.com/problems/maximum-subarray/description/
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # return self.getSubMax(nums, 0, len(nums))
        return self.greed(nums)

    def getSubMax(self, nums, left, right) -> int:
        if left == right - 1:
            return nums[left]

        mid = (right + left) >> 1

        # cal mid max
        mid_max = self.getMidMax(nums, left, mid, right)

        return max(self.getSubMax(nums, left, mid), self.getSubMax(nums, mid, right), mid_max)

    def getMidMax(self, nums, left, mid, right) -> int:
        left_max, right_max = 0, nums[mid]
        curr_sum = left_max
        i, j = mid - 1, mid + 1
        while i >= left:
            curr_sum += nums[i]
            left_max = max(left_max, curr_sum)
            i -= 1

        curr_sum = right_max
        while j < right:
            curr_sum += nums[j]
            right_max = max(right_max, curr_sum)
            j += 1

        return left_max + right_max

    def greed(self, nums) -> int:
        """
        As long as the previous sum is greater than 0, it is a positive contribution to the sum, otherwise it is directly reset curr sum
        """
        currSum, resMax = 0, float('-inf')
        for i in nums:
            currSum += i
            resMax = max(resMax, currSum)
            if currSum < 0:
                currSum = 0
        return resMax


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([5, 4, -1, 7, 8]))
    print(s.maxSubArray([4, -1, 2, 1, ]))
