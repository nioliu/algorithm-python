class Solution:
    def partitionString(self, s: str) -> int:
        curr_has = ""
        res = 1
        for i, v in enumerate(s):
            if v in curr_has:
                res += 1
                curr_has = ""
            curr_has += v
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.partitionString('abacaba'))
    print(s.partitionString('ssssss'))
