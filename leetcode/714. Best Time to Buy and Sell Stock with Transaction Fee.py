# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/?envType=daily-question&envId=2023-10-29
from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        貌似是个贪心问题？
        """
        # 初始情况
        cash = 0  # 没有股票
        hold = -prices[0]  # 持有一支股票

        for price in prices:
            # 在持有和不持有之间选择最大利润
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash

    def maxProfit1(self, prices: List[int], fee: int) -> int:
        """
        超出时间复杂度
        :param prices:
        :param fee:
        :return:
        """

        def action(index, boughtIndex, curr_profit):
            if index >= len(prices):
                self.res = max(self.res, curr_profit)
                return
            # no action
            action(index + 1, boughtIndex, curr_profit)
            # buy current
            if boughtIndex == -1:
                action(index + 1, index, curr_profit - prices[index])
            elif prices[index] - prices[boughtIndex] - fee > 0:
                # sell
                action(index + 1, -1, curr_profit + prices[index] - fee)

        action(0, -1, 0)
        return self.res

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        """
        超出空间复杂度
        """
        # dp = [[-1] * (len(prices)+1) for _ in range(len(prices)+1)]
        dp = {}

        def action(index, boughtIndex) -> int:
            """
            buy or sell
            return the max one
            """
            if index >= len(prices):
                return 0
            # if  dp[index][boughtIndex]!=-1:
            # return  dp[index][boughtIndex]
            if (index, boughtIndex) in dp:
                return dp[(index, boughtIndex)]
            curr_res = action(index + 1, boughtIndex)
            if boughtIndex == -1:
                # buy or no action
                curr_res = max(
                    action(index + 1, index),
                    curr_res
                )
            elif boughtIndex != -1 and prices[index] - prices[boughtIndex] - fee > 0:
                # sell or no aciton
                curr_res = max(
                    action(index + 1, -1) + prices[index] - prices[boughtIndex] - fee,
                    curr_res
                )
            # dp[index][boughtIndex] = curr_res
            dp[(index, boughtIndex)] = curr_res
            return curr_res

        return action(0, -1)
