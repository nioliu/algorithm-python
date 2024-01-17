# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return None
        slowP = head.next
        fastP = head.next.next

        while fastP and fastP.next:
            if slowP == fastP:
                slowP = head
                fastP = fastP
                while slowP != fastP:
                    slowP = slowP.next
                    fastP = fastP.next
                return slowP

            slowP = slowP.next
            fastP = fastP.next.next
        return None

