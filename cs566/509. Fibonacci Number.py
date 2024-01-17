class Solution:

    def __init__(self):
        self.a = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.a:
            return self.a[n]
        else:
            self.a[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.a[n]


if __name__ == '__main__':
    a = Solution()
    print(a.fib(3))
