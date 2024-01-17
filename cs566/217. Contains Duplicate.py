# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        use set to solve
        """
        res = set()
        for k in nums:
            if k in res:
                return True
            res.add(k)
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.containsDuplicate([1, 2, 3, 1]))
