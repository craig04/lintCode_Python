class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """

    def flatten(self, root):
        if not root:
            return None
        right = root.right
        root.right = self.flatten(root.left)
        root.left = None
        tail = root
        while tail.right:
            tail = tail.right
        tail.right = self.flatten(right)
        return root
