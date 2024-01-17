# https://leetcode.com/problems/coin-change/
from typing import List


class Solution:
    def __init__(self):
        self.quickCheck = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        return self.nextCoin(coins, amount)

    def nextCoin(self, coins, amount) -> int:
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        currRes = -1
        for i in range(int(amount // coins[-1]), -1, -1):
            if len(coins) == 1:
                if amount % coins[0] == 0:
                    return amount // coins[0]
                else:
                    return -1
            if amount in self.quickCheck:
                return self.quickCheck[amount]
            cost = self.nextCoin(coins[:len(coins) - 1], amount - i * coins[-1])
            if cost != -1:
                if currRes == -1:
                    currRes = cost + i
                else:
                    currRes = min(cost + i, currRes)
        self.quickCheck[amount] = currRes
        return currRes


if __name__ == '__main__':
    s = Solution()
    # print(s.coinChange([1, 2, 5], 11))
    # print(s.coinChange([186, 419, 83, 408], 6249))
    # 157 / 189 testcases passed
    print(s.coinChange([208, 170, 205, 425, 124, 375], 7130))
