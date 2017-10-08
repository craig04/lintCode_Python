class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: a: the root of binary tree a.
    @param: b: the root of binary tree b.
    @return: true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        if a and b:
            return a.val == b.val \
                   and self.isIdentical(a.left, b.left) \
                   and self.isIdentical(a.right, b.right)
        return not a and not b
