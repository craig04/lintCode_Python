class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        result = self.__max(root)[1]
        return 0 if result is None else result

    def __max(self, root):
        if root is None:
            return [0, None]
        resLeft = self.__max(root.left)
        maxLeft = max(0, resLeft[0])
        resRight = self.__max(root.right)
        maxRight = max(0, resRight[0])
        maxPath = maxLeft + maxRight + root.val
        if resLeft[1] is not None:
            maxPath = max(maxPath, resLeft[1])
        if resRight[1] is not None:
            maxPath = max(maxPath, resRight[1])
        return [max(maxLeft, maxRight) + root.val, maxPath]
