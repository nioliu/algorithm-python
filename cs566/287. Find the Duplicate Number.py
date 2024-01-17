from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        quickDic = {}
        for i in nums:
            if i in quickDic:
                return i
            else:
                quickDic[i] = 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))
