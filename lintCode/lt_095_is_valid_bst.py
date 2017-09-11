class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        return self.__isValid(root, [None])

    def __isValid(self, root, prev):
        if not root:
            return True
        if not self.__isValid(root.left, prev):
            return False
        if prev[0] is not None and prev[0] >= root.val:
            return False
        prev[0] = root.val
        return self.__isValid(root.right, prev)
