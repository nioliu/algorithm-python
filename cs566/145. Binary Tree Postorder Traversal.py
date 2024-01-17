# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s1 = [root]
        s2 = []
        while len(s1) > 0:
            curr = s1.pop()
            s2.append(curr)
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)

        res = []
        while len(s2) > 0:
            res.append(s2.pop().val)
        return res
