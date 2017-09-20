class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        mts = [[0] * (col + 1) for r in xrange(row + 1)]
        for r in xrange(row):
            for c in xrange(col):
                mts[r + 1][c + 1] = matrix[r][c] - mts[r][c] + \
                                    mts[r + 1][c] + mts[r][c + 1]
        for l in xrange(col):
            for t in xrange(row):
                for r in xrange(l, col):
                    for b in xrange(t, row):
                        if mts[b + 1][r + 1] + mts[t][l] - mts[b + 1][l] - mts[t][r + 1] == 0:
                            return [[t, l], [b, r]]
