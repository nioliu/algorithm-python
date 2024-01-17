# https://leetcode.com/problems/game-of-life/
import copy
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copyBoard = copy.deepcopy(board)
        for row in range(len(copyBoard)):
            for col in range(len(copyBoard[0])):
                currState = copyBoard[row][col]
                board[row][col] = 0
                neiA = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if ((i == 0 and j == 0) or
                                row + i < 0 or
                                row + i >= len(copyBoard) or
                                col + j < 0 or
                                col + j >= len(copyBoard[0])):
                            continue
                        if copyBoard[row + i][col + j] != 0:
                            neiA += 1
                if currState == 1:
                    if neiA == 2 or neiA == 3:
                        board[row][col] = 1
                else:
                    if neiA == 3:
                        board[row][col] = 1


if __name__ == '__main__':
    s = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s.gameOfLife(board)
    print(board)
