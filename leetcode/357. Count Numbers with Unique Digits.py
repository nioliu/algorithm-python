import sys


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 0
        quickCheck = []
        for i in range(0, pow(10, n)):
            curr = i
            currArr = []
            base = 10
            repeat = False
            while curr // base > 0:
                j = curr % base
                if j in currArr or curr in quickCheck:
                    repeat = True
                    break
                currArr.append(j)
                curr //= base
            if not repeat and curr not in currArr:
                res += 1
            else:
                quickCheck.append(i)
        print(quickCheck)
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.countNumbersWithUniqueDigits(4))
    n = sys.stdin.readline()
    for line in range(int(n)):
        curr = sys.stdin.readline().strip()
        s = 0
        for i in range(1, int(curr[0]) + 1):
            s += int(curr[i])
        print(s)
