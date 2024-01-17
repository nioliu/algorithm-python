# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def nextPathSum(currSum: int, currNode: TreeNode, currList: List):
            if currNode is None:
                return
            currSum += currNode.val
            currList.append(currNode.val)
            if currSum == targetSum:
                if currNode.left is None and currNode.right is None:
                    res.append(currList)
            nextPathSum(currSum, currNode.left, currList[:])
            nextPathSum(currSum, currNode.right, currList[:])

        nextPathSum(0, root, [])
        return res
