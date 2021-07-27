import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive traversal with valid range
class Solution:
    def validate_tree(self, root, from_=-math.inf, to_=math.inf):
        if root is None:
            return True
        if root.val <= from_ or root.val >= to_:
            return False
        return self.validate_tree(root.left, from_, root.val) and \
               self.validate_tree(root.right, root.val, to_)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate_tree(root)


# iterative traversal with valid range
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, from_, to_ = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= from_ or val >= to_:
                return False
            stack.append((root.left, from_, root.val))
            stack.append((root.right, root.val, to_))
        return True
