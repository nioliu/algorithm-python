# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/?envType=daily-question&envId=2023-10-10
import bisect
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/solutions/4152964/video-how-we-think-about-a-solution-python-javascript-java-c/?envType=daily-question&envId=2023-10-10
        写不出来，需要考虑的情况太多了，建议直接放弃。这个人也花了2小时才写出来。
        :param nums:
        :return:
        """
        length = len(nums)
        min_operations = length
        unique_nums = sorted(set(nums))
        right = 0

        for left in range(len(unique_nums)):
            while right < len(unique_nums) and unique_nums[right] < unique_nums[left] + length:
                right += 1
            bisect.bisect_right()
            min_operations = min(min_operations, length - (right - left))

        return min_operations
