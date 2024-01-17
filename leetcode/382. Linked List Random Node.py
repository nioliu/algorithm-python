# https://leetcode.com/problems/linked-list-random-node/
import random
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, headnode: Optional[ListNode]):
        self.head = headnode
        self.cnt = 0
        self.random = random.Random()
        while headnode:
            self.cnt += 1
            headnode = headnode.next

    def getRandom(self) -> int:
        index = self.random.randint(0, self.cnt - 1)
        node = self.head
        for _ in range(index + 1):
            node = node.next
        return node.val


class Solution2:
    """
    转换成数组
    """

    def __init__(self, head: Optional[ListNode]):
        self.ll = []
        while head:
            self.ll.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.ll[random.randint(0, len(self.ll) - 1)]


if __name__ == '__main__':
    head = ListNode(3, ListNode(4, ListNode(6)))
    obj = Solution2(head)
    for i in range(10 ^ 3):
        param_1 = obj.getRandom()
        print(param_1)
