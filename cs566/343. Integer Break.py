class Solution:
    def integerBreak(self, n: int) -> int:
        quickCheck = {}

        def pickNext(target, currMulti) -> int:
            """
            return current max multi
            """
            if target in quickCheck:
                return quickCheck[target] * currMulti

            if target == 0:
                return currMulti

            if target < 0:
                return -1

            currMax = currMulti
            for i in range(1, target + 1):
                if i == n:
                    continue

                subMax = pickNext(target - i, currMulti * i)
                if subMax == -1:
                    break

                currMax = max(currMax, subMax)

            quickCheck[target] = currMax
            return currMax

        return pickNext(n, 1)


if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(2))
