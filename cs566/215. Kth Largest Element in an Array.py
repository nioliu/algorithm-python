import random
from typing import List


# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        use heap to solve
        """

        # return self.findKthLargestQuickSort(nums, k, 0, len(nums))

        # heapify
        def heapify(nums2, n, index):
            l = (index << 1) + 1
            r = (index << 1) + 2
            minIndex = index
            if l < n and nums2[minIndex] > nums2[l]:
                minIndex = l
            if r < n and nums2[minIndex] > nums2[r]:
                minIndex = r
            if minIndex != index:
                nums2[minIndex], nums2[index] = nums2[index], nums2[minIndex]
                heapify(nums2, n, minIndex)

        minHeap = nums[:k]
        for i in range((len(minHeap) >> 1) - 1, -1, -1):
            heapify(minHeap, len(minHeap), i)

        for v in nums[k:]:
            if v > minHeap[0]:
                minHeap[0] = v
                heapify(minHeap, len(minHeap), 0)

        return minHeap[0]

    def findKthLargestQuickSort(self, nums, k, l, r):
        if r - l <= 1:
            return nums[l]

        markIndex = random.randint(l, r - 1)
        mark = nums[markIndex]  # 将第一个元素作为枢纽元素
        nums[markIndex], nums[l] = nums[l], nums[markIndex]
        pos = l  # mark's position
        for curr in range(l + 1, r):
            if nums[curr] < mark:
                pos += 1
                nums[pos], nums[curr] = nums[curr], nums[pos]

        nums[l], nums[pos] = nums[pos], nums[l]

        if r - pos > k:
            return self.findKthLargestQuickSort(nums, k, pos + 1, r)
        elif r - pos < k:
            return self.findKthLargestQuickSort(nums, k - (r - pos), l, pos)
        else:
            return mark


if __name__ == '__main__':
    # s = Solution()
    # print(s.findKthLargest([3, 5, 4, 1, 2, 9], 2))
    # print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    # print(s.findKthLargest([1], 1))
    # print(s.findKthLargest([2, 1], 1))
    # print(s.findKthLargest([7, 6, 5, 4, 3, 2, 1], 2))
    a = [1, 2, 4, 5]
    b = a[:2]
    b[0] = 3
    print(a, b)
