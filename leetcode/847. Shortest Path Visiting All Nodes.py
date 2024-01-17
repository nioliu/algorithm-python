import sys
from typing import List


class Solution:
    def __init__(self):
        self.res = sys.maxsize

    # dfs, not suitable, since it need the shortest path
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        for i in range(len(graph)):
            self.res = min(self.next(graph, [i], 0, len(graph)), self.res)
        return self.res

    def next(self, graph: List[List[int]], has, steps, aim) -> int:
        """
        maintain an array "has" to look if it could be recurse completely
        """
        if len(has) == aim:
            return steps

        curr = has[len(has) - 1]
        curr_next_indexes = graph[curr]
        small_steps = sys.maxsize
        for i in curr_next_indexes:
            curr_aim = aim
            if i in has:
                # find if it could be continued for all
                skip = False
                for k in range(len(has)):
                    if has[k] == i:
                        if k != 0 and has[k - 1] == curr:
                            skip = True
                            break
                if skip:
                    continue
                curr_aim += 1
            if curr_aim > self.res:
                continue
            has.append(i)
            small_steps = min(self.next(graph, has, steps + 1, curr_aim), small_steps)
            has.pop()
        return small_steps


if __name__ == '__main__':
    a = Solution()
    print([1, 2, 3, 4] == [1, 2, 3, 4])
    # print(a.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]))
    # print(a.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
    # print(a.shortestPathLength([[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9],
    #                             [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9],
    #                             [0, 1, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 8, 9],
    #                             [0, 1, 2, 3, 4, 5, 6, 7, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 11], [8], [9]]))
