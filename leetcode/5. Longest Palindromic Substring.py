class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        这几个变量，一个都不能省，每个都有存在的意义！！！不要试图省事！！！
        :param s:
        :return:
        """
        if len(s) <= 1:
            return s

        s = self.getMarchStr(s)
        largestIndex = 0  # the lagrset right index
        right = 0
        longArr = [0] * len(s)  # curr index palindrome's long
        res = s[0]
        resLen = 0

        for i in range(1, len(s)):
            if i < right:
                longArr[i] = min(right - i, longArr[2 * largestIndex - i])
            # find current palindrome length
            while i - longArr[i] - 1 >= 0 and i + longArr[i] + 1 < len(s) and s[i - longArr[i] - 1] == s[
                i + longArr[i] + 1]:
                longArr[i] += 1

            # statistic the result
            if resLen < longArr[i]:
                res = s[i - longArr[i]:i + longArr[i] + 1]
                resLen = longArr[i]

            # replace the largest index
            if longArr[i] + i > right:
                largestIndex = i
                right = longArr[i] + i

        return res.replace('#', '')

    def getMarchStr(self, s1: str):
        for i in range(len(s1)):
            s1 = s1[:2 * i] + "#" + s1[2 * i:]
        return s1 + "#"

    def longestPalindrome(self, s: str) -> str:
        """
        明明方法一样，为什么这个执行得更快呢？
        :param s:
        :return:
        """
        if len(s) <= 1:
            return s

        Max_Len = 1
        Max_Str = s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i] - 1] == s[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i - dp[i]:i + dp[i] + 1]
        return Max_Str.replace('#', '')


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        # 预处理字符串
        modified_s = "#" + "#".join(s) + "#"
        palindromeRecords = [0] * len(modified_s)
        center = 0
        rightBoundary = 0
        resCenter = 0

        for i in range(len(modified_s)):
            # 利用对称性优化回文半径的初始值
            if i < rightBoundary:
                mirror = 2 * center - i
                palindromeRecords[i] = min(rightBoundary - i, palindromeRecords[mirror])

            # 扩展回文半径
            a = i + palindromeRecords[i] + 1
            b = i - palindromeRecords[i] - 1
            while a < len(modified_s) and b >= 0 and modified_s[a] == modified_s[b]:
                palindromeRecords[i] += 1
                a += 1
                b -= 1

            # 更新中心和右边界
            if i + palindromeRecords[i] > rightBoundary:
                center = i
                rightBoundary = i + palindromeRecords[i]

            # 更新最长回文中心
            if palindromeRecords[i] > palindromeRecords[resCenter]:
                resCenter = i

        # 获取最长回文子串
        start = (resCenter - palindromeRecords[resCenter]) // 2
        end = start + palindromeRecords[resCenter]
        return s[start:end]


if __name__ == '__main__':
    s = Solution2()
    print(s.longestPalindrome("edcadbdace"))

    # print(s.getMarchStr("12324"))
