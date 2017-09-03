class Solution:
    """
    @param: matrix: A lsit of lists of integers
    @return:
    """

    def setZeroes(self, matrix):
        row = len(matrix)
        if row == 0 or len(matrix[0]) == 0:
            return matrix
        r = c = False
        col = len(matrix[0])
        rows = range(row)
        cols = range(col)
        row_ex_0 = range(1, row)
        col_ex_0 = range(1, col)
        for i in rows:
            if matrix[i][0] == 0:
                c = True
                break
        for j in cols:
            if matrix[0][j] == 0:
                r = True
                break
        for i in row_ex_0:
            for j in col_ex_0:
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in row_ex_0:
            if matrix[i][0] == 0:
                for j in col_ex_0:
                    matrix[i][j] = 0
        for j in col_ex_0:
            if matrix[0][j] == 0:
                for i in row_ex_0:
                    matrix[i][j] = 0
        if r:
            for j in cols:
                matrix[0][j] = 0
        if c:
            for i in rows:
                matrix[i][0] = 0
