class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):
        i = 0
        q = [[root, 0]]
        values = []
        while i != len(q):
            elem = q[i]
            node = elem[0]
            level = elem[1]
            i += 1
            if node:
                if len(values) == level:
                    values.append([])
                values[-1].append(node.val)
                q.append([node.left, level + 1])
                q.append([node.right, level + 1])
        values.reverse()
        return values
