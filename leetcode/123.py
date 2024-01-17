class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        for c in s1:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        i, j = 0, 0
        copyDic = dic.copy()
        while j - i < len(s1) and i <= j < len(s2):
            # 直接右指针向右移动
            if s2[j] in dic and dic[s2[j]] > 0:
                dic[s2[j]] -= 1
                j += 1
            else:
                # 重新开始
                if s2[j] not in dic:
                    i, j = j + 1, j + 1
                    dic = copyDic
                    copyDic = dic.copy()
                else:
                    # 否则找到上一个消耗点
                    while i <= j:
                        if s2[i] != s2[j]:
                            dic[s2[i]] += 1  # 还回去
                            i += 1  # 左指针右移
                        else:
                            break
                    i += 1
                    j += 1
        return j - i == len(s1)


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ky", "ainwkckifykxlribaypk"))