# https://leetcode.com/problems/validate-binary-tree-nodes/description/?envType=daily-question&envId=2023-10-17
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find the root firstly
        # root = 0
        has = set()

        # 循环寻找到尽头
        # while root in leftChild or root in rightChild:
        #     has.add(root)
        #     if root in leftChild:
        #         root = leftChild.index(root)
        #     else:
        #         root = rightChild.index(root)
        #     if root in has:
        #         return False

        # 更加快捷的方法
        def findRoot():
            children = set(leftChild + rightChild)
            for node in range(n):
                if node not in children:
                    return node
            return -1

        root = findRoot()
        # has.clear()
        has.add(root)
        stack = [root]
        while len(stack) > 0:
            currNode = stack.pop()
            leftNode = leftChild[currNode]
            rightNode = rightChild[currNode]
            if leftNode > -1:
                if leftNode in has:
                    return False
                stack.append(leftNode)
                has.add(leftNode)
            if rightNode > -1:
                if rightNode in has:
                    return False
                stack.append(rightNode)
                has.add(rightNode)
        return len(has) == n
