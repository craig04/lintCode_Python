class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @return: the new root
    """

    def convertBST(self, root):
        self.__convert(root, 0)
        return root

    def __convert(self, root, addi):
        if not root:
            return 0
        right = self.__convert(root.right, addi)
        sum = root.val + right
        root.val += right + addi
        left = self.__convert(root.left, root.val)
        return sum + left
