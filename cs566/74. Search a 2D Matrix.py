# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def next(rowFrom, rowEnd) -> bool:
            if rowFrom == rowEnd - 1 or matrix[rowFrom][-1] >= target:
                i, j = 0, len(matrix[rowFrom])
                while i < j:
                    mid = (i + j) >> 1
                    midV = matrix[rowFrom][mid]
                    if midV > target:
                        j = mid
                    elif midV < target:
                        i = mid + 1
                    else:
                        return True
                return False

            midRow = (rowFrom + rowEnd) >> 1
            if matrix[midRow][0] > target:
                return next(rowFrom, midRow)
            if matrix[midRow][0] < target:
                return next(midRow, rowEnd)
            return True

        return next(0, len(matrix))


if __name__ == '__main__':
    s = Solution()
    # print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
