class Solution:
    def factorial(self, n: int) -> int:  # implement Working Algorith
        if n == 1:
            return 1
        return self.factorial(n - 1) * n


if __name__ == '__main__':
    s = Solution()
    print(s.factorial(3))
