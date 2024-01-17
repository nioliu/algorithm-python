# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def formatFromArr(nums) -> Optional[ListNode]:
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    return head


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findTheMiddleNode(head: Optional[ListNode]):
            """
            find the middle node of the linked list
            """
            if head is None:
                return None, None
            preMiddle, middleP, doubleP = None, head, head
            while doubleP.next is not None and doubleP.next.next is not None:
                doubleP = doubleP.next.next
                preMiddle = middleP
                middleP = middleP.next
            return preMiddle, middleP

        # find the pre and middle node
        pre, middle = findTheMiddleNode(head)
        if middle is None:
            return None

        # set the middle as current root
        root = TreeNode(middle.val)

        # the right of the root is the right numbers of the middle
        root.right = self.sortedListToBST(middle.next)

        if pre is not None:
            pre.next = None
            root.left = self.sortedListToBST(head)

        return root

    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        change linked list to array to find the middle pointer quickly
        :param head:
        :return:
        """
        nums = []
        curr = head
        while curr is not None:
            nums.append(curr)
            curr = curr.next
        return self.sortedListToBSTInner(nums, 0, len(nums))

    def sortedListToBSTInner(self, nums: List, l, r) -> Optional[TreeNode]:
        if l >= r:
            return None
        # find the pre and middle node
        middleIndex = l + ((r - l) >> 1)
        middle = nums[middleIndex]

        # set the middle as current root
        root = TreeNode(middle.val)

        # the right of the root is the right numbers of the middle
        root.right = self.sortedListToBSTInner(nums, middleIndex + 1, r)
        # same as above
        root.left = self.sortedListToBSTInner(nums, l, middleIndex)

        return root


if __name__ == '__main__':
    s = Solution()
    head = formatFromArr([-10, -3, 0, 5, 9])
    res = s.sortedListToBST2(head)
    print(res)
