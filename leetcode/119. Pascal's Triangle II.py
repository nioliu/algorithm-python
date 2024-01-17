# https://leetcode.com/problems/pascals-triangle-ii/description/
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            pre = 1
            for j in range(1, len(res) ):
                temp = res[j]
                res[j] = pre + res[j]
                pre = temp
            # add a 1 to the last
            res.append(1)
            print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    s.getRow(3)
