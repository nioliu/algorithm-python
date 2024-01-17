class Solution:
    def __init__(self):
        self.res = None
        self.base = pow(10, 9) + 7

    def countOrders(self, n: int) -> int:
        """
        -1 represent to p1, +1 represent to d1
        out of time limit
        """
        hasSet = set()
        self.res = 0

        def pickNext():
            if len(hasSet) == 2 * n:
                self.res += 1
                return

            for i in range(1, n + 1):
                if -i in hasSet and i not in hasSet:
                    hasSet.add(i)
                    pickNext()
                    hasSet.remove(i)
                if -i not in hasSet:
                    hasSet.add(-i)
                    pickNext()
                    hasSet.remove(-i)

        pickNext()
        return self.res % self.base


if __name__ == '__main__':
    s = Solution()
    print(s.countOrders(6))
