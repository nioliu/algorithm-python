# https://leetcode.com/problems/sort-characters-by-frequency/
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        mem = {}
        for i in s:
            if i not in mem:
                mem[i] = 1
            else:
                mem[i] += 1
        bigHeap = []
        for k, v in mem.items():
            heapq.heappush(bigHeap, (-v, k))
        res = ""
        while len(bigHeap) > 0:
            v, k = heapq.heappop(bigHeap)
            res += k * -v
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort("tree"))
    print(s.frequencySort("cccaaa"))
    print(s.frequencySort("Aabb"))
