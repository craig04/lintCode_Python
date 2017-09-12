import sys


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The maximum number in the interval [start, end]
    """

    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.max
        mid = (root.start + root.end) >> 1
        result = -sys.maxint - 1
        if start <= mid:
            result = max(result, self.query(
                root.left, start, min(end, mid)))
        if end > mid:
            result = max(result, self.query(
                root.right, max(mid + 1, start), end))
        return result
