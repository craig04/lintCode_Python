class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        reverse = False
        layer = [root]
        result = []
        while layer:
            nextLayer = []
            value = []
            for node in layer:
                if node:
                    value.append(node.val)
                    nextLayer.append(node.left)
                    nextLayer.append(node.right)
            if reverse:
                value.reverse()
            reverse = not reverse
            result.append(value)
            layer = nextLayer
        result.pop()
        return result
