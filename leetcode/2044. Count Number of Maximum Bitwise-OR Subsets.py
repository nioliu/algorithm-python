# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
from collections import defaultdict
from typing import List


class Solution:
    """
    这种子序列的，都需要用递归解决，while循环太麻烦了
    并且这种递归是无法转换成while的，因为子过程不需要返回值，是在递归的途中进行统计返回的
    """

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        # 效率会稍微快一点
        orDic = defaultdict(int)

        def pick(i, currOr):
            if i >= len(nums):
                # statistic
                orDic[currOr] += 1
                return

            pick(i + 1, currOr | nums[i])  # pick current
            pick(i + 1, currOr)  # don't pick current

        pick(1, nums[0])
        pick(1, 0)

        return max(orDic.values())


class Solution1:
    def __init__(self):
        self.currMax = None

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        orDic = {}
        self.currMax = nums[0]

        def pick(i, currOr):
            if i >= len(nums):
                # statistic
                if currOr in orDic:
                    orDic[currOr] += 1
                else:
                    orDic[currOr] = 1
                self.currMax = max(currOr, self.currMax)
                return

            pick(i + 1, currOr | nums[i])  # pick current
            pick(i + 1, currOr)  # don't pick current

        pick(1, nums[0])
        pick(1, 0)

        return orDic[self.currMax]


if __name__ == '__main__':
    s = Solution()
    # print(s.countMaxOrSubsets([3, 2, 1, 5]))
    print(s.countMaxOrSubsets([2, 2, 2]))
