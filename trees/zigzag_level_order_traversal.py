# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        level = [root]
        left_to_right = True
        while level:
            next_level = []
            values = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                values.append(node.val)
            if left_to_right:
                result.append(values)
            else:
                result.append(values[::-1])
            left_to_right = not left_to_right
            level = next_level
        return result
