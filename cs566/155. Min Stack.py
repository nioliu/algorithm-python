# https://leetcode.com/problems/min-stack/description/
class MinStack:
    def __init__(self):
        self.nums = []

    def push(self, val: int) -> None:
        if len(self.nums) == 0:
            self.nums.append((val, val))
        else:
            self.nums.append((val, min(self.nums[-1][1], val)))

    def pop(self) -> None:
        self.nums = self.nums[:-1]

    def top(self) -> int:
        if len(self.nums) == 0:
            return None
        return self.nums[-1][0]

    def getMin(self) -> int:
        return self.nums[-1][1]
