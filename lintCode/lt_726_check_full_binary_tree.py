class Solution:
    """
    @param: : the given tree
    @return: Whether it is a full tree
    """

    def isFullTree(self, root):
        return root is not None and (
            (not root.left and not root.right) or
            (self.isFullTree(root.left) and self.isFullTree(root.right)))
