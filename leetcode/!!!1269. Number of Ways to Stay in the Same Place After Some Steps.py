# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/?envType=daily-question&envId=2023-10-15


class Solution:
    def __init__(self):
        self.quickCheck = {}
        self.base = pow(10, 9) + 7

    def numWays(self, steps: int, arrLen: int) -> int:
        return self.next(steps, 0, arrLen) % self.base

    def next(self, steps: int, currIndex: int, arrLen: int) -> int:
        if steps == 0:
            if currIndex == 0:
                return 1
            return 0
        if (steps, currIndex) in self.quickCheck:
            return self.quickCheck[(steps, currIndex)]
        res = 0
        for i in range(-1, 2):
            if 0 <= currIndex + i < arrLen:
                res += self.next(steps - 1, currIndex + i, arrLen)
        self.quickCheck[(steps, currIndex)] = res
        return res


class Solution:
    def __init__(self):
        self.base = pow(10, 9) + 7

    def numWays(self, steps: int, arrLen: int) -> int:
        maxPosition = min(arrLen - 1, steps)  # 最多只可能到达steps
        dp = [[0] * (maxPosition + 1) for _ in range(steps + 1)]  # 也就递归的两个变化的参数：steps: int, currIndex: int

        # Initialize the base case
        dp[0][0] = 1

        # 外层递归循环
        for i in range(1, steps + 1):
            # 内层position循环
            # 这里实际上就是遍历每个位置，获取每个位置在steps步下，可以有多少种到达终点的方式
            for j in range(maxPosition + 1):
                dp[i][j] = dp[i - 1][j]

                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % self.base

                if j < maxPosition:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % self.base

        return dp[steps][0]
