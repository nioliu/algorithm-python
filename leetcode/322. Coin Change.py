# https://leetcode.com/problems/coin-change/description/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        res = amount + 1
        for i in coins:
            if i > amount:
                continue
            subMin = self.coinChange(coins, amount - i)
            if subMin != -1:
                res = min(res, subMin + 1)
        return res if res <= amount else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a < c:
                    break
                else:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
