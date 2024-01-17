# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        核心：不用去关心怎么具体怎么排列的，当前递归只关心：我的左右子树是谁，返回根节点
        """

        if not inorder or not preorder:
            return None
        currRoot = TreeNode(preorder[0])
        rootIndex = inorder.index(
            currRoot.val)  # find the range index for curr root to search the left tree and right tree

        currRoot.left = self.buildTree(preorder[1:rootIndex + 1], inorder[:rootIndex])
        currRoot.right = self.buildTree(preorder[rootIndex + 1:], inorder[rootIndex + 1:])

        return currRoot


if __name__ == '__main__':
    s = Solution()
    res = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(res)
