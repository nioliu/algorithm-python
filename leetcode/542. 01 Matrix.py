# https://leetcode.com/problems/01-matrix/?envType=daily-question&envId=2023-11-04
import math
from collections import deque, defaultdict
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        时间复杂度太高了
        """
        res = [[float('inf')] * len(mat[0]) for _ in range(len(mat))]
        xd = [-1, 1, 0, 0]
        yd = [0, 0, -1, 1]

        def find(i, j, visited) -> int:
            if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
                return float('inf')
            if mat[i][j] == 0:
                res[i][j] = 0
                return 0

            curr_res = float('inf')
            for p in range(4):
                if (i + xd[p], j + yd[p]) not in visited:
                    visited.append((i + xd[p], j + yd[p]))
                    curr_res = min(curr_res, find(i + xd[p], j + yd[p], visited) + 1)
                    visited.pop()
            res[i][j] = curr_res
            return curr_res

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if res[i][j] == float('inf'):
                    find(i, j, [])
        return res


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        queue = deque()
        MAX_VALUE = m * n

        # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            # 遍历每一个已知距离的位置
            row, col = queue.popleft()
            for dr, dc in directions:
                # 检查它的附近的所有位置，如果当前距离更小，则更新
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    # 如果小，则更新，并且重新入队列，因为可能r，c附近的会使其他也会变得更小
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1

        return mat


if __name__ == '__main__':
    s = Solution()
    # print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
    # print(s.updateMatrix([[0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]))
    print(s.updateMatrix([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 1], [1, 1, 1, 1, 0], [1, 0, 0, 1, 0]]))
