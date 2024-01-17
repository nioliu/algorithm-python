# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None

        left = root.left
        # move the left to the right of root, and move the original right to the right of the rightest
        if left is not None:
            right = root.right
            root.right = left
            rightest = left
            # find the rightest of the left node
            while rightest.right is not None:
                rightest = rightest.right
            rightest.right = right
            root.left = None  # clear the left of the root
        # just flatten the next right
        self.flatten(root.right)
