from typing import List


class Solution:
    def reverse_stack(self, arr: List):
        """
        逆序一个stack，不使用额外空间，只允许递归
        """
        if len(arr) == 0:
            return
        lastV = arr.pop()
        self.reverse_stack(arr)
        self.insert_stack(lastV, arr)

    def insert_stack(self, v, arr: List):
        """
        加之前，先清空stack，然后再加v，然后将其他v再加进去，将v压入栈底部
        """
        if len(arr) == 0:
            arr.append(v)
            return
        currV = arr.pop()
        self.insert_stack(v, arr)
        arr.append(currV)


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    print(s.reverse_stack(a))
    print(a)
