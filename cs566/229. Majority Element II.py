# https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        aim = length // 3
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

            if dic[i] == aim + 1:
                nums.append(i)

        return nums[length:]
