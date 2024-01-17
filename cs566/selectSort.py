def selection_sort(nums):
    for i in range(len(nums)):
        curr_min = nums[i]
        curr_min_index = i
        # find the smallest value an index
        for k in range(i + 1, len(nums)):
            if nums[k] < curr_min:
                curr_min_index = k
                curr_min = nums[k]
        # swap i index and minimum index
        if curr_min_index != i:
            swap(nums, curr_min_index, i)
    return nums


def swap(nums, i, j):
    nums[i] ^= nums[j]
    nums[j] ^= nums[i]
    nums[i] ^= nums[j]


print(selection_sort([1,5,2,3,9,4,7]))
