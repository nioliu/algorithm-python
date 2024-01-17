class Solution:

    def mergeSort(self, nums):
        self.nextMerge(nums, 0, len(nums))
        return nums

    def nextMerge(self, nums, left, right):
        print(f'curr left: {left} and right: {right}')
        if left >= right - 1:
            return

        # partition, remember it should be right - left
        middle = ((right - left) >> 1) + left
        self.nextMerge(nums, left, middle)
        self.nextMerge(nums, middle, right)

        # merge
        self.merge2(nums, left, middle, right)

    def merge(self, nums, left, middle, right):
        # left - middle and middle - right are ordered
        right_index = middle
        left_index = left

        # any of these two condition is false, it could be broken.
        # since the smaller numbers has been move forward,
        # the rest numbers are the smaller and has been moved back.
        while left_index < middle and right_index < right:
            if nums[left_index] < nums[right_index]:
                left_index += 1
            else:
                # take right_index to the left_index position, and move back btw left_index and right_index
                curr_small_v = nums[right_index]
                for i in range(right_index, left_index, -1):
                    nums[i] = nums[i - 1]
                nums[left_index] = curr_small_v
                middle += 1
                left_index += 1
                right_index += 1

    def merge2(self, nums, left, middle, right):
        left_array = nums[left:middle]
        right_array = nums[middle:right]

        merged_array = []
        i = j = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                merged_array.append(left_array[i])
                i += 1
            else:
                merged_array.append(right_array[j])
                j += 1

        while i < len(left_array):
            merged_array.append(left_array[i])
            i += 1

        while j < len(right_array):
            merged_array.append(right_array[j])
            j += 1

        nums[left:right] = merged_array


if __name__ == '__main__':
    s = Solution()
    print(s.mergeSort([1, 3, 4, 2, 6, 3, 7, 4]))
