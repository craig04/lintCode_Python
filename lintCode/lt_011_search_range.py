class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        result = []
        self.__search(root, k1, k2, result)
        return result

    def __search(self, root, k1, k2, result):
        if root is None:
            return
        val = root.val
        if k1 <= val:
            self.__search(root.left, k1, k2, result)
        if k1 <= val <= k2:
            result.append(val)
        if val <= k2:
            self.__search(root.right, k1, k2, result)
