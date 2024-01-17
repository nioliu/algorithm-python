# https://leetcode.com/problems/binary-tree-maximum-path-sum/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    超过了时间复杂度，但是应该是正确的
    主要是递归里面需要递归很多次，某些还需要返回，比较乱，后面可以尝试尝试驴一下思路
    """

    def __init__(self):
        self.res = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.res = root.val

        def nextLayer(currNode: Optional[TreeNode], currSum) -> int:
            if currNode is None:
                return currSum
            if currSum == -1001:
                currSum = currNode.val
            else:
                currSum += currNode.val
            self.res = max(self.res, currSum)
            # left with root
            sublr = nextLayer(currNode.left, currSum)
            # right with root
            subrr = nextLayer(currNode.right, currSum)
            # only left
            if currNode.left:
                nextLayer(currNode.left, -1001)
            # only right
            if currNode.right:
                nextLayer(currNode.right, -1001)
            # left + right + root
            self.res = max(self.res, sublr + subrr - currSum * 2 + currNode.val)

            return max(sublr, subrr, currSum)

        # left or right or without root value
        lr = nextLayer(root.left, root.val)
        rr = nextLayer(root.right, root.val)
        print(lr, rr)
        if root.left:
            nextLayer(root.left, -1001)
        if root.right:
            nextLayer(root.right, -1001)

        self.res = max(self.res, lr + rr - root.val)

        return self.res


class Solution:
    """
    官方题解，貌似不需要考虑但个节点的情况，如果子树的和比0小，那么就是单个节点
    hard难度的题别想复杂了
    """

    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")  # placeholder to be updated

        def get_max_gain(node):
            nonlocal max_path  # This tells that max_path is not a local variable
            if node is None:
                return 0

            gain_on_left = max(get_max_gain(node.left), 0)  # Read the part important observations

            gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations

            current_max_path = node.val + gain_on_left + gain_on_right  # Read first three images of going down the recursion stack
            max_path = max(max_path, current_max_path)  # Read first three images of going down the recursion stack

            return node.val + max(gain_on_left, gain_on_right)  # Read the last image of going down the recursion stack

        get_max_gain(root)  # Starts the recursion chain
        return max_path
