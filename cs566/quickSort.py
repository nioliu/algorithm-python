from cs566.bubbleSort import swap


def quickSort(nums):
    if len(nums) == 1:
        return nums
    quickNext(nums, 0, len(nums))
    return nums


def quickNext(nums, begin, end):
    if begin >= end - 1:
        return
    main_v = nums[begin]  # set the beginning is the main
    pos = findPos(nums, main_v, begin + 1, end)
    nums[begin] = nums[pos]
    nums[pos] = main_v
    quickNext(nums, begin, pos)
    quickNext(nums, pos + 1, end)


# find right position for v, return the index
def findPos(nums, v, begin, end) -> int:
    """
    寻找v应当在的位置
    :param nums: 原数组
    :param v: 标志值
    :param begin: 数组开始位置
    :param end: 数组结束为止
    :return: v应当在的位置
    """
    end = end - 1
    while begin < end:
        # 找到第一个比当前位置大的元素
        while begin < end and nums[begin] < v:
            begin += 1
        # 找到最后一个比当前位置小的元素
        while begin < end and nums[end] > v:
            end -= 1
        if end == begin:
            break
        # 调换位置
        swap(nums, begin, end)
        # 更新坐标，继续寻找
        begin += 1
        end -= 1
    return begin


if __name__ == '__main__':
    print(quickSort([1, 3, 2, 4, 5, 6, 1, 2]))
