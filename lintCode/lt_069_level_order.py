class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        i = 0
        Q = [[root, 0]]
        values = []
        while i != len(Q):
            elem = Q[i]
            node = elem[0]
            level = elem[1]
            i += 1
            if node:
                if len(values) == level:
                    values.append([])
                values[-1].append(node.val)
                Q.append([node.left, level + 1])
                Q.append([node.right, level + 1])
        return values
