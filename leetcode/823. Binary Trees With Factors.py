# https://leetcode.com/problems/binary-trees-with-factors/description/?envType=daily-question&envId=2023-10-26
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.append(1)
        arr.sort()
        dp = [-1] * len(arr)

        def pickNext(root, end) -> int:
            """
            pick children to be root and return the methods
            """
            if end <= 0 or root == 1:
                return 1
            if dp[end] != -1:
                return dp[end]
            curr_res = 0
            for i in range(end, 0, -1):
                if root % arr[i] == 0 and root // arr[i] in arr:
                    index = arr.index(root // arr[i])
                    if index == 0:
                        curr_res += 1
                    else:
                        curr_res += pickNext(arr[i], i) * pickNext(root / arr[i], index)
            dp[end] = curr_res
            return curr_res

        res = 0
        for i in range(len(arr) - 1, 0, -1):
            res += pickNext(arr[i], i)

        return res % (pow(10, 9) + 7)

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = [1] * (len(arr))
        MOD = (pow(10, 9) + 7)
        res = 0
        for i in range(len(arr)):
            for j in range(i, -1, -1):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in arr:
                    # 这一步太费时间了
                    index = arr.index(arr[i] // arr[j])
                    dp[i] += dp[j] * dp[index]
            res += dp[i] % MOD

        return res % MOD

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        from gpt
        :param arr:
        :return:
        """
        arr.sort()
        mod = 10 ** 9 + 7
        dp = {}

        for i, num in enumerate(arr):
            dp[num] = 1
            for j in range(i):
                if num % arr[j] == 0 and num // arr[j] in dp:
                    dp[num] += dp[arr[j]] * dp[num // arr[j]]
                    dp[num] %= mod

        return sum(dp.values()) % mod


if __name__ == '__main__':
    s = Solution()
    print(s.numFactoredBinaryTrees(
        [2, 4, 10, 20]))
