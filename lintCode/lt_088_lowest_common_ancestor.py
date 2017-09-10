class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        return self.__search(root, A, B)[1]

    def __search(self, root, A, B):
        if root is None:
            return [0, None]
        found = 0
        found |= 1 if A == root else 0
        found |= 2 if B == root else 0
        if found == 3:
            return [3, root]
        [val, _] = left = self.__search(root.left, A, B)
        if val == 3:
            return left
        found |= val
        [val, _] = right = self.__search(root.right, A, B)
        if val == 3:
            return right
        found |= val
        return [found, root if found == 3 else None]
