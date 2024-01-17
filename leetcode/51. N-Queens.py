from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.chooseNext(n, 0, 0, 0, 0, [])
        return self.res

    def chooseNext(self, n, row, col, ld, rd, res: List[str]):
        """
        选择下一个存放n皇后的位置
        :param n: 最大行数
        :param res: 当前的结果存放
        :param row: 当前行
        :param col: 不能选用的列
        :param ld: 不能选用的左对角线
        :param rd: 不能选用的右对角线
        """
        if row >= n:
            self.res.append(res[:])  # 复制数组
            return
        # 计算可以选用的位置
        # 注意限制 avaPos 的长度,((1 << n) - 1)必须有，否则不知道avaPos的位数，的出来的结果是0
        avaPos = ~(col | ld | rd) & ((1 << n) - 1)
        while avaPos:
            currAvaPos = avaPos & -avaPos  # 获取最低位的 1
            avaPos &= avaPos - 1  # 移除最低位的 1
            pos = bin(currAvaPos).count("0") - 1  # 计算 'Q' 的位置
            self.chooseNext(n, row + 1, col | currAvaPos, (ld | currAvaPos) << 1, (rd | currAvaPos) >> 1,
                            res + ["." * pos + "Q" + "." * (n - pos - 1)])  # 构建当前行字符串并递归


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
