from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursiveInorderDFS:
    def inorder(self, root: Optional[TreeNode], traversal: List[int]) -> List[int]:
        if root is None:
            return traversal
        self.inorder(root.left, traversal)
        traversal.append(root.val)
        self.inorder(root.right, traversal)
        return traversal

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = self.inorder(root, [])
        return traversal[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
