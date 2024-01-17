# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        isNeg = False
        if x <= 0:
            isNeg = True
            x = -x
        base = 10
        while x != 0:
            stack.append(x % base)
            x //= base
        res = 0
        base = 1
        while stack:
            res += stack.pop() * base
            base *= 10
        if isNeg:
            res = -res
        return res if -pow(2, 31) < res < pow(2, 31) - 1 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
