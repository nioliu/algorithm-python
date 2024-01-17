# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        res = self.stack2[-1]
        return res

    def empty(self) -> bool:
        return not self.stack2 and not self.stack
