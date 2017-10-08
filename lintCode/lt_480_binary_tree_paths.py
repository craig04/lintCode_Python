class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        paths = []
        if not root:
            return paths
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)
        if not paths:
            paths.append(str(root.val))
        return paths
