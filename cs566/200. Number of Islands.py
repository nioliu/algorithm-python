# https://leetcode.com/problems/number-of-islands/description/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def infect(grid: List[List[str]], i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            infect(grid, i - 1, j)
            infect(grid, i + 1, j)
            infect(grid, i, j - 1)
            infect(grid, i, j + 1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    infect(grid, i, j)
                    res += 1
        return res
