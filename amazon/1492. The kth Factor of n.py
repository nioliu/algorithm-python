# https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        if k == 1:
            return 1
        has = [1, n]
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                if int(n / i) == i:
                    has.insert(int(len(has) / 2), int(n / i))
                if i in has:
                    break
                has.insert(int(len(has) / 2), int(n / i))
                has.insert(int(len(has) / 2), i)

                if cnt == k:
                    return i
        if k <= len(has):
            return has[k - 1]
        return -1


if __name__ == '__main__':
    a = Solution()
    print(a.kthFactor(12, 3))
    print(a.kthFactor(7, 2))
    print(a.kthFactor(4, 4))
