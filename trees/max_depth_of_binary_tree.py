class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node {self.val}, left: {self.left.val or None}, right: {self.right.val or None}'


# recursive DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return True
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# iterative DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [(1, root)]
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth


# iterative BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
        return depth
