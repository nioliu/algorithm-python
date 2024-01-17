# https://leetcode.com/problems/parallel-courses-iii/description/?envType=daily-question&envId=2023-10-18
from typing import List


class Solution:
    def __init__(self):
        self.relations = List[List[int]]
        self.time = []
        self.preDict = {}
        self.quickCheck = []

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        1. find all the terminal coures
        2. recurse each pre courses for the curr terminal course
        3. maintaince a set to store courses has been on
        4. add all the courses that don't have any pre course
        """
        self.relations = relations
        self.time = time
        self.quickCheck = [-1 for _ in range(n)]
        arr = [0 for _ in range(n)]  # mark the index if is a terminal course, 1 stand for no
        self.preDict = {}  # to record the pre courses
        for i in relations:
            arr[i[0] - 1] = 1
            if i[1] - 1 in self.preDict:
                self.preDict[i[1] - 1].append(i[0] - 1)
            else:
                self.preDict[i[1] - 1] = [i[0] - 1]
        res = 0
        for i in range(len(arr)):
            # need to take all the courses, so return the max one
            if arr[i] == 0:
                res = max(res, self.preTake(i))
        return res

    def preTake(self, currCourse) -> int:
        """
        return  the minimal times to take all the pre course
        """
        if currCourse not in self.preDict:
            return self.time[currCourse]
        if self.quickCheck[currCourse] != -1:
            return self.quickCheck[currCourse]
        res = 0
        for preCourse in self.preDict[currCourse]:
            res = max(self.preTake(preCourse) + self.time[currCourse], res)
        self.quickCheck[currCourse] = res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]))
    print(s.minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]))
    i1 = [[0] for _ in range(2)]
    i2 = [0 for _ in range(3)]
    i3 = [[0] * 3 for _ in range(2)]
    i4 = [0] * 5
    print(i1)
    print(i2)
    print(i3)
    print(i4)
