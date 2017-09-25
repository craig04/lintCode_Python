from sys import maxint


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        if not root:
            return 0
        depth = self.minDepth(root.left) if root.left else maxint
        if root.right:
            depth = min(depth, self.minDepth(root.right))
        return 1 if depth == maxint else depth + 1
