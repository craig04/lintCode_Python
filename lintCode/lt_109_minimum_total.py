import sys


class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        for r in range(1, len(triangle)):
            row = triangle[r]
            prev = triangle[r - 1]
            for i in range(len(row)):
                add = prev[i - 1] if i else sys.maxint
                if i != len(row) - 1:
                    add = min(add, prev[i])
                row[i] += add
        return min(triangle[-1])
