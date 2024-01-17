# https://leetcode.com/problems/delete-and-earn/description/
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def deleteNext(has_delete, start) -> int:
            """
            return the max points if remove all the delete elments
            """
            if len(has_delete) == len(nums) or start >= len(nums):
                return 0
            curr_res = 0
            for i in range(start, len(nums)):
                if nums[i] in has_delete:
                    continue
                has_delete.add(nums[i] - 1)
                has_delete.add(nums[i] + 1)
                curr_res = max(curr_res, deleteNext(has_delete, i + 1) + nums[i])
                if nums[i] + 1 in has_delete:
                    has_delete.remove(nums[i] + 1)
                if nums[i] - 1 in has_delete:
                    has_delete.remove(nums[i] - 1)
            return curr_res

        return deleteNext(set(), 0)


if __name__ == '__main__':
    s = Solution()
    # print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
