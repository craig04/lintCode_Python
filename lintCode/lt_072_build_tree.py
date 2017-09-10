class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: inorder: A list of integers that inorder traversal of a tree
    @param: postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """

    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        val = postorder[-1]
        node = TreeNode(val)
        index = inorder.index(val)
        node.left = self.buildTree(
            inorder[:index], postorder[:index])
        node.right = self.buildTree(
            inorder[index + 1:], postorder[index:len(postorder) - 1])
        return node
