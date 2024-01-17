from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        mem = [[[None] * len(grid) for _ in range(len(grid))] for _ in range(len(grid))]

        def pick(i1, i2, j1):
            """
            i1,i2 is the porsiont of the people1
            j1,j2 is people2
            return cherries can pick up for this position
            """
            j2 = i1 + j1 - i2
            if i1 < 0 or j1 < 0 or i2 < 0 or j2 < 0 or i1 >= len(grid) or j1 >= len(grid) or i2 >= len(
                    grid) or j2 >= len(grid) or grid[i1][j1] == -1 or grid[i2][j2] == -1:
                return float('-inf')

            if mem[i1][i2][j1] is not None:
                return mem[i1][i2][j1]

            if i1 == i2 == j1 == len(grid) - 1:
                return grid[i1][i2]

            cherries = grid[i1][i2]
            if i1 != j1:
                cherries += grid[j1][j2]

            cherries += max(
                pick(i1 + 1, i2, j1 + 1),  # p1 and p2 go down
                pick(i1 + 1, i2, j1),  # p1 go down and p2 go right
                pick(i1, i2 + 1, j1 + 1),  # p1 go right and p2 go down
                pick(i1, i2 + 1, j1)  # p1 go right and p2 go right
            )

            mem[i1][i2][j1] = cherries
            return cherries

        return pick(0, 0, 0)


if __name__ == '__main__':
    grid = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
    s = Solution()
    s.cherryPickup(grid)
