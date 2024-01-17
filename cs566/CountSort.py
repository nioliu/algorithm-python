from typing import List


def countSort(heights: List):
    maxV = max(heights)
    cnt = [0] * (maxV + 1)
    for i in heights:
        cnt[i] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]
    res = [0] * len(heights)
    for i in range(len(heights) - 1, -1, -1):
        pos = cnt[heights[i]]
        res[pos - 1] = heights[i]
        cnt[heights[i]] -= 1
    return res


if __name__ == '__main__':
    print(countSort([1, 2, 3, 4, 2, 3, 2, 0]))
