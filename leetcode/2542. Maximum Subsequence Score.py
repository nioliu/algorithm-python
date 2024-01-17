# https://leetcode.com/problems/maximum-subsequence-score/?envType=daily-question&envId=2023-10-09
from typing import List


class Solution:
    def __init__(self):
        self.res = None

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        self.res = float('-inf')

        def pickNext(start: int, currK: int, currSumOf1: int, currMinOf2: int):
            """
            pick the next value
            这个递归无法使用dp，因为是从上到下进行推算的，上层不需要下层的信息，因此也无法使用记忆化搜索什么的
            """
            if currK == 0:
                self.res = max(currMinOf2 * currSumOf1, self.res)
            else:
                for i in range(start, len(nums1)):
                    pickNext(i + 1, currK - 1, currSumOf1 + nums1[i], min(currMinOf2, nums2[i])),

        pickNext(0, k, 0, pow(10, 5) + 1)
        return self.res


class Solution2:
    """
    不太正确，不能取子序列的最大乘积作为返回。
    因为父序列的和可能会变化，例如：
    当子序列的返回是：（10，2）or（5，5），会返回（5，5）=25，大于（10，2）=20
    而父序列是：（100，2）更想要的是（10，2），所以不正确
    """

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        quickCheck = {}

        def pickNext(start, currK, beforeMin) -> (int, int):
            """
            从start开始选择，返回子序列的对应乘积最大值的sumOf1和minOf2
            """
            if currK == 0:
                return 0, pow(10, 5) + 1

            subRes = set()
            if (start, currK) in quickCheck:
                subRes = quickCheck[(start, currK)]
            maxSum = 0
            minValue = pow(10, 5) + 1
            maxV = float('-inf')
            for i in range(start, len(nums1)):
                # 选择子序列最大乘积，只有当记忆化搜索中的min大于当前min时，继续向下递归
                if not subRes or subRes[1] > min(beforeMin, nums2[i]):
                    subRes = pickNext(i, currK - 1, min(beforeMin, nums2[i]))
                subSum = subRes[0] + nums1[i]
                subMin = min(subRes[1], nums2[i])
                if maxV < (subSum * subMin):
                    maxV = subSum * subMin
                    maxSum = subSum
                    minValue = subMin
            quickCheck[(start, currK)] = (maxSum, minValue)
            return quickCheck[(start, currK)]

        res = pickNext(0, k, pow(10, 5) + 1)
        return res[0] * res[1]


if __name__ == '__main__':
    s = Solution2()
    print(s.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))
    print(s.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1))
    print(s.maxScore([44, 10, 25, 0, 25, 49, 0], [18, 39, 15, 31, 43, 20, 45], 6))
    print(s.maxScore(
        [93, 463, 179, 2488, 619, 2006, 1561, 137, 53, 1765, 2304, 1459, 1768, 450, 1938, 2054, 466, 331, 670, 1830,
         1550, 1534, 2164, 1280, 2277, 2312, 1509, 867, 2223, 1482, 2379, 1032, 359, 1746, 966, 232, 67, 1203, 2474,
         944, 1740, 1775, 1799, 1156, 1982, 1416, 511, 1167, 1334, 2344],
        [345, 229, 976, 2086, 567, 726, 1640, 2451, 1829, 77, 1631, 306, 2032, 2497, 551, 2005, 2009, 1855, 1685, 729,
         2498, 2204, 588, 474, 693, 30, 2051, 1126, 1293, 1378, 1693, 1995, 2188, 1284, 1414, 1618, 2005, 1005, 1890,
         30, 895, 155, 526, 682, 2454, 278, 999, 1417, 1682, 995], 42))
