from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res = []
        limit = 2 ** 31

        def pick(i, pre1, pre2):
            """
            i is the current index
            pre1 is the last number
            pre2 is the last number of pre1
            """
            if i >= len(num):
                return True
            if num.startswith(str(pre1 + pre2), i):
                res.append(int(pre1 + pre2))
                return pick(i + len(str(res[-1])), pre1 + pre2, pre1)
            return False

        # 第一个字符串的长度
        for l1 in range(1, len(num)):
            # 第二个字符串的长度
            for l2 in range(1, len(num) - l1):
                res = [int(num[:l1]), int(num[l1:l1 + l2])]
                if pick(l1 + l2, int(num[l1:l1 + l2]), int(num[:l1])):
                    return res
                res = []
                # 如果是0开头，那么就只能是0             
                if num[l1] == '0' or l1 + l2 > len(num) // 2 + 1:
                    break
            if num[0] == '0' or l1 > len(num) // 2 + 1:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.splitIntoFibonacci("1101111"))
