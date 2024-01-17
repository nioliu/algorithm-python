from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,6,7,1,2]
        :param nums:
        :return:
        """
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) >> 1
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return nums[mid + 1]
            # if i<mid, it is ascending from i to mid, so jump to [mid,j]
            elif nums[i] < nums[mid]:
                i = mid
            # else if i>mid, the minimum is in [i,mid]
            else:
                j = mid
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([1, 0]))
