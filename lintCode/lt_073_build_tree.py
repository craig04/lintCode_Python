class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """

    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        val = preorder[0]
        node = TreeNode(val)
        index = inorder.index(val)
        node.left = self.buildTree(
            preorder[1:index + 1], inorder[0:index])
        node.right = self.buildTree(
            preorder[index + 1:], inorder[index + 1:])
        return node
