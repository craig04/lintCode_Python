class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        values = []
        self.__traverse(root, values)
        return values

    def __traverse(self, root, values):
        if not root:
            return
        self.__traverse(root.left, values)
        values.append(root.val)
        self.__traverse(root.right, values)
