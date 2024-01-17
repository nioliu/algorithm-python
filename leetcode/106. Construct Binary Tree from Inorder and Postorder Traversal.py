# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # 后序遍历的最后一个元素是根节点的值
        root = TreeNode(postorder.pop())
        rootIndex = inorder.index(root.val)

        # 递归构建右子树和左子树（注意先构建右子树，再构建左子树）
        root.right = self.buildTree(inorder[rootIndex + 1:], postorder)
        root.left = self.buildTree(inorder[:rootIndex], postorder)

        return root


if __name__ == '__main__':
    s = Solution()
    res = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(res)
