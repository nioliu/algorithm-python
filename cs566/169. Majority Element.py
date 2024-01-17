from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()  # 2,3,3
        curr_nums = 1
        curr_max = 1
        res = nums[0]
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == nums[i - 1]:
                curr_nums += 1
            else:
                if curr_max < curr_nums:
                    curr_max = curr_nums
                    res = nums[i - 1]
                curr_nums = 1
        return res

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    a = Solution()
    print(a.majorityElement2([1, 1, 2, 3, 4]))
