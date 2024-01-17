# https://leetcode.com/discuss/interview-question/3113182/AMAZON-OA-or-SDE-INTERN-2023
from typing import List


class Solution:
    def getMaximumGreyness(self, arr: List[List]) -> int:
        """
        Time complexity: O(n)
        :param arr:
        :return:
        """
        rows = [0] * len(arr)
        cols = [0] * len(arr[0])
        for index in range(len(arr)):
            row = arr[index]
            for v in row:
                if v == 0:
                    v = -1
                rows[index] += v
        for index in range(len(arr[0])):
            for k in range(len(arr)):
                if arr[k][index] == 0:
                    arr[k][index] = -1
                cols[index] += arr[k][index]
        print(rows, cols)
        res = float('-inf')
        for i in rows:
            for j in cols:
                res = max(res, i + j)
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.getMaximumGreyness([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]))
    print(s.getMaximumGreyness([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
    print(type([123,123]))
