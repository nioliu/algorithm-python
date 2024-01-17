from typing import List


class Solution:
    # use queue to enumerate all the possible, this will take time complex O(n^2) .
    def minOperations(self, nums: List[int], x: int) -> int:
        # a queue for storing the next leftmost and rightmost and the rest of x
        next_pos = [[0, len(nums) - 1, x]]
        while len(next_pos) != 0:
            curr = next_pos.pop(0)
            if curr[0] > curr[1]:
                return -1
            if curr[2] - nums[curr[0]] == 0:
                return self.calSteps(curr[0], curr[1] + 1, nums)
            elif curr[2] - nums[curr[0]] > 0:
                next_pos.append([curr[0] + 1, curr[1], curr[2] - nums[curr[0]]])

            if curr[2] - nums[curr[1]] == 0:
                return self.calSteps(curr[0] - 1, curr[1], nums)
            elif curr[2] - nums[curr[1]] > 0:
                next_pos.append([curr[0], curr[1] - 1, curr[2] - nums[curr[1]]])
        return -1

    def calSteps(self, left, right, num):
        return left + 1 + len(num) - right


class Solution2:
    # use slide window to solve
    # https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/solutions/4066422/96-51-sliding-window/?envType=daily-question&envId=2023-09-20
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        left = 0
        curr_sum = 0
        max_len = 0
        for right, cal in enumerate(nums):
            curr_sum += cal
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len else -1


if __name__ == '__main__':
    a = Solution()
    # print(a.minOperations([1, 1, 4, 2, 3], 5))
    # print(a.minOperations([5, 6, 7, 8, 9], 4))
    # print(a.minOperations([3, 2, 20, 1, 1, 3], 10))
    # print(a.minOperations([1, 2], 10))
    print(a.minOperations(
        [1241, 8769, 9151, 3211, 2314, 8007, 3713, 5835, 2176, 8227, 5251, 9229, 904, 1899, 5513, 7878, 8663, 3804,
         2685, 3501, 1204, 9742, 2578, 8849, 1120, 4687, 5902, 9929, 6769, 8171, 5150, 1343, 9619, 3973, 3273, 6427, 47,
         8701, 2741, 7402, 1412, 2223, 8152, 805, 6726, 9128, 2794, 7137, 6725, 4279, 7200, 5582, 9583, 7443, 6573,
         7221, 1423, 4859, 2608, 3772, 7437, 2581, 975, 3893, 9172, 3, 3113, 2978, 9300, 6029, 4958, 229, 4630, 653,
         1421, 5512, 5392, 7287, 8643, 4495, 2640, 8047, 7268, 3878, 6010, 8070, 7560, 8931, 76, 6502, 5952, 4871, 5986,
         4935, 3015, 8263, 7497, 8153, 384, 1136], 894887480))
