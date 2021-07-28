class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
    def is_node_symmetric(self, node_l: TreeNode, node_r: TreeNode) -> bool:
        if node_l is None and node_r is None:
            return True
        if node_l is None or node_r is None:
            return False
        if node_l.val != node_r.val:
            return False
        return self.is_node_symmetric(node_l.right, node_r.left) and \
               self.is_node_symmetric(node_l.left, node_r.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_node_symmetric(root.left, root.right)


class SolutionIterative:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            node_l, node_r = stack.pop()
            if node_l is None and node_r is None:
                continue
            if node_l is None or node_r is None:
                return False
            if node_l.val != node_r.val:
                return False
            stack.append((node_l.left, node_r.right))
            stack.append((node_l.right, node_r.left))
        return True
