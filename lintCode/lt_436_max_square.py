class Solution:
    """
    @param: matrix: a matrix of 0 and 1
    @return: an integer
    """

    def maxSquare(self, matrix):
        if not any((any(e == 1 for e in row)) for row in matrix):
            return 0
        row = len(matrix)
        col = len(matrix[0])
        side = min(row, col)
        flag = [[matrix[i][j] == 1 for j in range(0, col)] for i in range(0, row)]
        for s in xrange(2, side + 1):
            found = False
            for i in xrange(row - s + 1):
                for j in xrange(col - s + 1):
                    flag[i][j] &= flag[i + 1][j] & flag[i][j + 1] & flag[i + 1][j + 1]
                    found |= flag[i][j]
            if not found:
                return (s - 1) * (s - 1)
        return side * side
