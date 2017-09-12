class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        return self.__generate(range(1, n + 1))

    def __generate(self, values):
        if not values:
            return [None]
        roots = []
        for i in range(len(values)):
            for left in self.__generate(values[:i]):
                for right in self.__generate(values[i + 1:]):
                    root = TreeNode(values[i])
                    root.left = left
                    root.right = right
                    roots.append(root)
        return roots
