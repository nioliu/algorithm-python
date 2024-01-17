# https://leetcode.com/problems/k-th-symbol-in-grammar/?envType=daily-question&envId=2023-10-25


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        0 0+1 01+10 0110+1001 01101001+10010110
        """
        if k == 1:
            return 0
        if k % 2 == 0:
            return 1 if self.kthGrammar(n - 1, k // 2) == 0 else 0
        else:
            return self.kthGrammar(n - 1, k // 2 + k % 2)


if __name__ == '__main__':
    s = Solution()
    # print(s.kthGrammar(2, 2))
    # print(s.kthGrammar(1, 1))
    # print(s.kthGrammar(2, 1))
    # print(s.kthGrammar(30, 434991989))
    print(s.kthGrammar(3, 4))
