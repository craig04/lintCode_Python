class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        if not root:
            return None
        node = root
        left = self.maxNode(root.left)
        if left and node.val < left.val:
            node = left
        right = self.maxNode(root.right)
        if right and node.val < right.val:
            node = right
        return node
