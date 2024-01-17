# Implement Data Structure called Heap
# Please implement the function create_heap() which takes as an input list of numbers and returns the Heap
# Please implement the function heapify(), which takes as an input list of numbers, length and index and performs heapify

def heapify(nums, n, i):
    curr_v = nums[i]
    left_index = (i << 1) + 1
    right_index = (i << 1) + 2
    curr_max_index = i
    if left_index < n and nums[left_index] < curr_v:
        curr_max_index = left_index
    if right_index < n and nums[right_index] < nums[curr_max_index]:
        curr_max_index = right_index
    if curr_max_index != i:
        nums[i], nums[curr_max_index] = nums[curr_max_index], nums[i]
        heapify(nums, n, curr_max_index)


def create_heap(ls):
    for i in range((len(ls) >> 1) - 1, -1, -1):
        heapify(ls, len(ls), i)
    return ls


# Implement HeapSort
# Please implement the function which takes as an input list of numbers and sorts it using HeapSort
# You can use create_heap() function from above
def heap_sort(ls):
    ls = create_heap(ls)
    m = len(ls)
    res = []
    for i in range(m - 1, -1, -1):
        res.append(ls[0])
        ls[i], ls[0] = ls[0], ls[i]
        heapify(ls, i, 0)

    return res


if __name__ == '__main__':
    # print(create_heap([5, 4, 3, 2, 10]))
    print(heap_sort([5, 4, 3, 2, 10]))
