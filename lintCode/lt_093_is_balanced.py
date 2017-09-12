class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        return self.__isBalanced(root)[0]

    def __isBalanced(self, root):
        if root is None:
            return True, 0
        balanced, left = self.__isBalanced(root.left)
        if not balanced:
            return False, 0
        balanced, right = self.__isBalanced(root.right)
        if not balanced or abs(left - right) > 1:
            return False, 0
        return True, max(left, right) + 1
