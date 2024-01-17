# insert sort
# find a right place for current value
# when you find, just swap them.
def insertion_sort(nums):
    for i in range(1, len(nums)):
        curr_v = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > curr_v:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = curr_v


if __name__ == '__main__':
    a = [5,4,3,2,10]
    insertion_sort(a)
    print(a)
