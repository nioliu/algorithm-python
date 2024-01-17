class Solution:
    def kmp(self, s1: str, s2: str) -> bool:
        """
        判断是否s2在s1内部
        """
        auxArr = self.auxArr(s2)
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
                continue
            elif j > 0:
                j = auxArr[j]  # 利用辅助数组跳过已比较的部分
            else:
                i += 1

        return len(s2) == j

    def auxArr(self, s):
        """
        获取s的辅助数组，每个位置的前缀和后缀相等的最大长度
         a  a  a  b  c  d  a  a  a  b  c  d  a  a  a
        -1  0  1  2  0  0  0  1  2  3  4  5  6  7  8
        """
        auxArr = [0] * len(s)  # 代表当前位置之前的前缀后缀相等的最大长度
        auxArr[0] = -1
        for i, c in enumerate(s):
            if i == 0 or i == 1:
                continue
            preIndex = i - 1
            preChar = s[i - 1]
            while preIndex > 0:
                if s[auxArr[preIndex]] == preChar:
                    auxArr[i] = auxArr[preIndex] + 1
                    break
                else:
                    preIndex = auxArr[preIndex]
        return auxArr


if __name__ == '__main__':
    s = Solution()
    # print(s.kmp("aaabcdaabcdaaaff", "aaabcdaaabcdaaa"))
    print(s.auxArr("aaabcdaaabcdaaacc"))
