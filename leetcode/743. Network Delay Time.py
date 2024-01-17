from typing import List


class Solution:
    def __init__(self):
        self.nextDict = {}
        self.minCost = float('inf')

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        for i in times:
            if i[0] not in self.nextDict:
                self.nextDict[i[0]] = {i[1]: i[2]}
            else:
                self.nextDict[i[0]][i[1]] = i[2]
        print(self.nextDict)
        return


if __name__ == '__main__':
    a = set()
    times = [[2, 1, 1], [1, 2, 3], [1, 3, 2]]
    s = Solution()
    s.networkDelayTime(times, 1, 1)
