from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        res = []
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            lastLeft = stack.pop()
            res.append(lastLeft.val)
            curr = lastLeft.right
        return res
