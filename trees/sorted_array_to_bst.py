from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionIterative:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])
        stack = list()
        stack.append((root, nums[0:mid], True))
        stack.append((root, nums[mid+1:], False))
        while stack:
            parent, lst, is_left = stack.pop()
            if not lst:
                continue
            n = len(lst)
            mid = n // 2
            node = TreeNode(lst[mid])
            if is_left:
                parent.left = node
            else:
                parent.right = node
            stack.append((node, lst[0:mid], True))
            stack.append((node, lst[mid+1:], False))
        return root


class Solution:
    def build(self, nums, low, high):
        if low == high:
            return TreeNode(nums[low])
        elif low < high:
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            node.left = self.build(nums, low, mid-1)
            node.right = self.build(nums, mid+1, high)
            return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums) - 1)
