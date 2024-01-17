# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        begin = head
        for _ in range(n):
            begin = begin.next
        pre = None
        remove = head
        while begin:
            pre = remove
            remove = remove.next
            begin = begin.next
        if pre:
            pre.next = remove.next
        else:
            head = head.next
        return head
