base = pow(10, 9) + 7


def getPrefixScores(arr):
    if len(arr) == 1:
        return [arr[0] * 2]

    # get the prefix most value
    currMax = arr[0]
    maxIndex = [currMax]  # first i index's max index
    for i, v in enumerate(arr):
        if i == 0:
            continue
        currMax = max(currMax, v)
        maxIndex.append(currMax)

    res = [2 * arr[0]]
    lastMax = res[0]
    for i in range(1, len(arr)):
        currNums = arr[:i + 1]
        if maxIndex[i] > maxIndex[i - 1]:
            currSum = 0
            for j in range(i + 1):
                currNums[j] += currNums[j - 1]
                currSum += currNums[j]
            res.append(currSum % base)
            lastMax = currNums[i]
        else:
            lastMax = lastMax + arr[i]
            res.append((res[i - 1] + lastMax) % base)
    return res


def getPrefixScores2(arr):
    res = []
    for i in range(len(arr)):
        currNums = arr[:i + 1]
        currMaxV = max(currNums)
        for j in range(i + 1):
            currNums[j] += currMaxV
            # if curr sum greater than the max, then replace it
            currMaxV = max(currNums[j], currMaxV)
        res.append(sum(currNums) % base)
    return res


if __name__ == '__main__':
    print(getPrefixScores([5, 1, 4, 2, 5, 3, 1, 54]))
    print(getPrefixScores2([5, 1, 4, 2, 5, 3, 1, 54]))
    # print(getPrefixScores([1]))
