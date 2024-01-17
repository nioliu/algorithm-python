from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # bigHeap = []
        # smallHeap = []
        medianPos = ((len(nums1) + len(nums2)) >> 1) + 1  # stop at the last one
        preV, currV = -1, -1
        i, j = 0, 0
        while i + j < medianPos:
            # return directly
            if i >= len(nums1):
                return nums2[medianPos - i - j]
            elif j >= len(nums2):
                return nums1[medianPos - i - j]
            # get the smaller one
            preV = currV
            currMin = nums1[i]
            if nums2[j] < currMin:
                currMin = nums2[j]
                j += 1
            else:
                i += 1
            currV = currMin

            # insert into heap
            # if len(bigHeap) > len(smallHeap) + 1:
        if len(nums2) + len(nums1) % 2 == 1:
            return preV
        return (preV + currV) / 2


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
