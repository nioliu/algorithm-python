# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        if len(intervals) <= 1:
            return intervals
        end = len(intervals)
        i = 1
        res = [intervals[0]]
        while i < end:
            pairs = intervals[i]
            if not (pairs[0] > res[-1][1]):
                res[-1][1] = max(pairs[1], res[-1][1])
                res[-1][0] = min(pairs[0], res[-1][0])
            else:
                res.append(pairs)
            i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [8, 10], [2, 6], [15, 18]]))
    print(s.merge([[1, 4], [2, 3]]))
