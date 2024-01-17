def bubblesort(nums):
    for k in range(len(nums)):
        for i in range(len(nums) - k - 1):
            if nums[i] > nums[i + 1]:
                swap(nums, i, i + 1)
    return nums


def swap(nums, i, j):
    nums[i] ^= nums[j]
    nums[j] ^= nums[i]
    nums[i] ^= nums[j]


if __name__ == '__main__':
    print(bubblesort([1, 2, 4, 2, 3, 5, 2, 1, 9, 10, 6]))
