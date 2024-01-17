from bisect import bisect_right, bisect_left
from typing import List


# https://leetcode.com/problems/number-of-flowers-in-full-bloom/?envType=daily-question&envId=2023-10-11

class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort(key=lambda value: (value[0], -value[1]))  # sort by value[0], if same, by value[1] decrease
        res = []
        for arrDay in people:
            currRes = 0
            for bloomDay in flowers:
                if bloomDay[0] > arrDay:
                    break
                if bloomDay[1] >= arrDay:
                    currRes += 1
            res.append(currRes)
        return res


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]


if __name__ == '__main__':
    s = Solution()
    print(s.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
