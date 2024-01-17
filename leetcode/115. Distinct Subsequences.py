# https://leetcode.com/problems/distinct-subsequences/description/
from functools import cache


class Solution:
    def __init__(self):
        self.charDict = {}
        self.res = 0
        self.quickCheck = {}  # key: begin position; value: {t's index : ways}

    def numDistinct(self, s: str, t: str) -> int:
        for i in range(len(s)):
            if s[i] not in self.charDict:
                self.charDict[s[i]] = [i]
            else:
                self.charDict[s[i]].append(i)

        self.find(s, t, 0, -1)
        return self.res

    def find(self, s, t, atT, begin):
        """
        find the possible next char position
        """
        if atT >= len(t):
            self.res += 1
            return

        # if quick check has current condition, then just return it,
        # cause the only two variables are atT and begin
        if begin in self.quickCheck and atT in self.quickCheck[begin]:
            self.res += self.quickCheck[begin][atT]
            return

        aimChar = t[atT]
        currRes = self.res
        if aimChar in self.charDict:
            aimCharIndexes = self.charDict[aimChar]
            for i in aimCharIndexes:
                if len(s) - i <= len(t) - atT:
                    if s[i:] == t[atT:]:
                        self.res += 1
                    break

                if i > begin:
                    self.find(s, t, atT + 1, i)

        # statistic the result, as current res for quick check
        currRes = self.res - currRes
        if begin in self.quickCheck:
            self.quickCheck[begin][atT] = currRes
        else:
            self.quickCheck[begin] = {atT: currRes}


if __name__ == '__main__':
    s = Solution()
    # print(s.numDistinct("rabbbit", "rabbit"))
    print(s.numDistinct("babgbag", "bag"))
    # print(s.numDistinct("b", "a"))
