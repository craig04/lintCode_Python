class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    """
    @param: A: a list of integer
    @return: The root of Segment Tree
    """

    def build(self, A):
        return self.__build(A, 0, len(A) - 1) if A else None

    def __build(self, A, left, right):
        if left == right:
            return SegmentTreeNode(left, right, A[left])
        mid = (left + right) >> 1
        root = SegmentTreeNode(left, right, 0)
        root.left = self.__build(A, left, mid)
        root.right = self.__build(A, mid + 1, right)
        root.max = max(root.left.max, root.right.max)
        return root
