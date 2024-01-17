# https://leetcode.com/problems/powx-n/description/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n > 0:
            for i in range(n):
                res *= x
        else:
            for i in range(n, 0, 1):
                res /= x
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(-2, 2))
