from typing import List

"""
主要是理解记忆化搜索转while的能力
"""


# https://leetcode.com/problems/max-dot-product-of-two-subsequences/?envType=daily-question&envId=2023-10-08
class Solution1:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        quickCheck = {}
        globalMin = -1000 * 1000 - 1

        def pickNext(n1: int, n2: int) -> int:
            """
            选择nums1和nums2位于n1和n2之后的位置（包含）
            :return: 先择当前位置后，子序列的最大乘积
            """
            # 超过范围后，直接返回最小的，理论上不会到这里
            if n1 >= len(nums1) or n2 >= len(nums2):
                return 0

            if (n1, n2) in quickCheck:
                return quickCheck[(n1, n2)]

            # 其中一个到达最后面了
            if n1 == len(nums1) or n2 == len(nums2):
                return nums1[n1] * nums2[n2]

            currMax = nums1[n1] * nums2[n2]
            for i in range(n1, len(nums1)):
                for j in range(n2, len(nums2)):
                    # 三种情况：
                    # 1. i*j 抛弃后面
                    # 2. i*j ➕ 后面
                    # 3. 不要当前也不要后面
                    currMax = max(currMax, nums1[i] * nums2[j] + pickNext(i + 1, j + 1), nums1[i] * nums2[j])
            quickCheck[(n1, n2)] = currMax
            return currMax

        return pickNext(0, 0)


class Solution2:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """
        由递归转变而来
        """
        m, n = len(nums1), len(nums2)
        globalMin = -1000 * 1000 - 1
        dp = [[globalMin] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        dp[m][n] = 0  # 等价于递归的结束条件: if n1 >= len(nums1) or n2 >= len(nums2): return 0

        # 观察递归的推导过程，本题中就是从后面往前推，所以这里递归的顺序也是从后往前
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                # 这里就等价于 currMax = max(currMax, nums1[i] * nums2[j] + pickNext(i + 1, j + 1), nums1[i] * nums2[j])
                dp[i][j] = max(
                    nums1[i] * nums2[j],
                    dp[i + 1][j + 1] + nums1[i] * nums2[j],
                    # 下面两个需要加上
                    dp[i][j + 1],
                    dp[i + 1][j]
                )

        # 这里就是递归的入口
        return dp[0][0]


class Solution3:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[float('-inf')] * m for _ in range(n)]

        def dp(i, j):
            if i == n or j == m:
                return float('-inf')

            if memo[i][j] != float('-inf'):
                return memo[i][j]

            memo[i][j] = max(
                nums1[i] * nums2[j] + dp(i + 1, j + 1),  # 选择当前
                nums1[i] * nums2[j],  # 不选任何
                dp(i + 1, j),  # 不选i
                dp(i, j + 1),  # 不选j
            )

            return memo[i][j]

        return dp(0, 0)


class Solution4:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        globalMin = -1000 * 1000 - 1
        dp = [[globalMin] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    nums1[i - 1] * nums2[j - 1],  # 匹配当前位置
                    dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1],  # 继续前一个子序列的乘积
                    dp[i - 1][j],  # 舍弃 nums1 的当前位置
                    dp[i][j - 1]  # 舍弃 nums2 的当前位置
                )

        return dp[m][n]


"""
首先，回顾一下记忆化搜索版本的核心逻辑：

python
currMax = nums1[n1] * nums2[n2]
for i in range(n1, len(nums1)):
    for j in range(n2, len(nums2)):
        currMax = max(currMax, nums1[i] * nums2[j] + pickNext(i + 1, j + 1), nums1[i] * nums2[j])

quickCheck[n1][n2] = currMax
return currMax
在这个逻辑中，pickNext(n1, n2) 返回以 (n1, n2) 为起点的子序列的最大点积。我们可以观察到以下规律：

当前位置 (n1, n2) 的最大点积 currMax 取决于三种情况：

以 (n1, n2) 为起点的点积 nums1[n1] * nums2[n2]
继续前一个子序列的点积 nums1[i] * nums2[j] + pickNext(i + 1, j + 1)
舍弃当前位置的点积 pickNext(n1 + 1, n2) 和 pickNext(n1, n2 + 1)（这里省略了数组越界检查）
我们希望求得的是以 (n1, n2) 为起点的最大点积 currMax。

基于上述观察，我们可以得出状态转移方程：

Copy code
dp[n1][n2] = max(
    nums1[n1] * nums2[n2],  # 匹配当前位置
    nums1[i] * nums2[j] + dp[i + 1][j + 1],  # 继续前一个子序列的点积
    dp[n1 + 1][n2],  # 舍弃 nums1 的当前位置
    dp[n1][n2 + 1]  # 舍弃 nums2 的当前位置
)
这个状态转移方程描述了在 (n1, n2) 位置的最大点积，它考虑了当前位置匹配、继续前一个子序列、舍弃当前位置的情况。

将这个状态转移方程应用到动态规划表格中，就可以有效地计算出最大的点积，而无需递归。这是将记忆化搜索转换为动态规划的一般方法之一，通过将递归中的状态和状态转移方程映射到动态规划表格中。
"""

if __name__ == '__main__':
    s = Solution3()
    print(s.maxDotProduct([2, 1, -2, 5], [3, 0, -6]))
    print(s.maxDotProduct([3, -2], [2, -6, 7]))
    print(s.maxDotProduct([-1, -1], [1, 1]))
    print(s.maxDotProduct([-5, -1, -2], [3, 3, 5, 5]))
    print(s.maxDotProduct([-7, -9, -1, 2, 2, 5, -7, 2, -7, 5], [7, 2, 2, -1, -1, 1, -4, 7, 6]))
    print(s.maxDotProduct(
        [-41, 6, 29, 50, -40, -67, -49, -19, -51, 93, 5, -12, -24, 51, -33, -29, -89, 26, -7, -75, -65, 19, 57, 51, 61,
         -96, -87, -12, -16, -49, -93, -96, 72, 92, 41, -76, 99, 56, -43, 16, -73, 19, -1, -7, -71, -68, -6, -82, 76,
         -3, -58, 42, 91, 8, 23, 87, 81, -37, 87, 98, 39, -40, 61, 36, -63, -70, 72, 100, -22, -52, -52, 93, 37, -76,
         -80, 59, 46, -52, 90, 6, -93, 95, -29, -79, 51, -44, -40, 99, 8, 53, -51, -41, 44, 30, -29, -97],
        [-44, -66, 50, -86, -96, 40, -70, -69, -52, -3, 59, -84, 97, 31, 9, -78, 5, -44, 63, -68, 82, 46, -82, 61, -80,
         -82, -67, -60, 52, 96, 96, 70, 49, -71, 98, -61, 68, -31, 72, -67, -1, 74, -25, 76, -86, 90, 27, 36, -49, -63,
         -83, -24, 80, -31, 88, 48, -87, -14, 82, -65, -100, -71, 47, 35, -43, -85, -86, 62, 85, 80, -71, 9, -30, -55,
         -79, -79, 29, 15, -7, 23, 39, 21, -45, -84, 25, 97, 57, 8, 3, 83, 32, -64, 1, 92, -44, 80, 34, -89, -16, 50]))
