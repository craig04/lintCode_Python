from sys import maxint


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class STNode(object):
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left = self.right = None


class Solution:
    """
    @param: A: An integer array
    @param: queries: An query list
    @return: The result list
    """

    def intervalMinNumber(self, A, queries):
        root = self.__build(A, 0, len(A) - 1)
        result = []
        for q in queries:
            result.append(self.__query(root, q.start, q.end))
        return result

    def __build(self, A, start, end):
        root = STNode(start, end, A[start])
        if start != end:
            mid = (start + end) >> 1
            root.left = self.__build(A, start, mid)
            root.right = self.__build(A, mid + 1, end)
            root.val = min(root.left.val, root.right.val)
        return root

    def __query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.val
        mid = (root.start + root.end) >> 1
        val = maxint if start > mid else self.__query(
            root.left, start, min(end, mid))
        if end > mid:
            val = min(val, self.__query(
                root.right, max(mid + 1, start), end))
        return val
