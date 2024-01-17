from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        targets = set()  # if current target has been calculated, then skip it
        for i in range(len(nums)):
            target = -nums[i]
            if target in targets:
                continue
            targets.add(target)
            l, r = i + 1, len(nums) - 1

            while i < l < r < len(nums):
                currSum = nums[l] + nums[r]
                if currSum == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    r -= 1

        return list(res)


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([0, 0, 0, 0]))
