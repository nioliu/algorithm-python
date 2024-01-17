"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from typing import Optional


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        queue = [root]
        layer = 1  # current layer to calculate current layer's nodes counts
        while len(queue) > 0:
            preNode = None  # set all the next

            # get all the current nodes
            for _ in range(pow(2, layer - 1)):
                currNode = queue.pop(0)

                if preNode is not None:
                    preNode.next = currNode
                preNode = currNode

                if currNode.left:
                    queue.append(currNode.left)
                    queue.append(currNode.right)

            preNode.next = None
            layer += 1
        return root
