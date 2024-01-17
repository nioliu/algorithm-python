from typing import List


# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) < 0:
            return 0

        quickDict = {}

        def nextJump(lastI, row) -> int:
            if row >= len(triangle):
                return 0

            if row in quickDict and lastI in quickDict[row]:
                return quickDict[row][lastI]

            currMinRes = min(triangle[row][lastI] + nextJump(lastI, row + 1),
                             triangle[row][lastI + 1] + nextJump(lastI + 1, row + 1))

            if row in quickDict:
                quickDict[row][lastI] = currMinRes
            else:
                quickDict[row] = {lastI: currMinRes}

            return currMinRes

        return triangle[0][0] + nextJump(0, 1)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
