# https://leetcode.com/problems/top-k-frequent-elements/description/
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntDict = {}
        # count the numbers of i
        for i in nums:
            if i not in cntDict:
                cntDict[i] = 1
            else:
                cntDict[i] += 1
        # the res, set the initial value is extraV
        # res = [extraV] * k
        # for k, v in cntDict.items():
        #     currMinIndex = 0
        #     for index, value in enumerate(res):
        #         # find the minimum index
        #         if value == extraV:
        #             currMinIndex = index
        #             break
        #         if cntDict[res[currMinIndex]] > cntDict[value]:
        #             currMinIndex = index
        #     # if bigger, then change it
        #     if v > cntDict[res[currMinIndex]]:
        #         res[currMinIndex] = k
        heap = []
        for num, freq in cntDict.items():
            if len(heap) < k:
                # it is a min-heap, based on [0] value
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))

        res = [elem[1] for elem in heap]
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    # print(s.topKFrequent([1], 1))
    # print(s.topKFrequent([-1, -1], 1))
    # print(s.topKFrequent([1, 2], 2))
    print(s.topKFrequent([3, 0, 1, 0], 1))
