# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def next(node):
            res.append(node.val)
            if node.left:
                next(node.left)
            if node.right:
                next(node.right)

        if root:
            next(root)
        return res


class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr and len(stack) > 0:
            while curr:
                res.append(curr)
                stack.append(curr)
                curr = curr.left
            last = stack.pop()
            curr = last.right

        return res
