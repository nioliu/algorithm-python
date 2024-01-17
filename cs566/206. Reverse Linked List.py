# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pre = head
        curr = head.next
        pre.next = None  # otherwise it will be a cycle
        while curr:
            currNext = curr.next
            curr.next = pre
            pre = curr
            curr = currNext
        return pre
