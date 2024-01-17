# https://leetcode.com/problems/height-checker/
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        maxV = max(heights)
        cnt = [0] * (maxV + 1)
        for i in heights:
            cnt[i] += 1
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i - 1]
        errorCnt = 0
        for i in range(len(heights) - 1, -1, -1):
            pos = cnt[heights[i]]
            if not (cnt[heights[i] - 1] <= i <= pos - 1):
                errorCnt += 1
            else:
                cnt[heights[i]] -= 1

        return errorCnt


if __name__ == '__main__':
    s = Solution()
    print(s.heightChecker([1, 2, 1, 2, 1, 1, 1, 2, 1]))
