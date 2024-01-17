from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        这里使用是使用了三路快排的算法：
        记住这个模版
        """
        r, w, b = 0, 0, len(nums) - 1  # 代表的是下一个可用的位置
        while w <= b:
            # 如果是第一个区域的元素，那么第一和第二区域都需要+1
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            # 如果是第二个区域的位置，只需要将第二个区域+1
            elif nums[w] == 1:
                w += 1
            # 如果是最后一个区域的位置，那么将第二个区域和第三个区域的位置交换位置，然后最后一个区域-1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
                # 这里w不++，是因为不知道nums[w]这个位置应该在哪里，所以下次还要继续判断


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 1, 2, 0, 0]
    s.sortColors(nums)
    print(nums)
