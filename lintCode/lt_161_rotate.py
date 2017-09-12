class Solution:
    """
    @param: matrix: a lists of integers
    @return:
    """

    def rotate(self, matrix):
        t, b = 0, len(matrix) - 1
        while t < b:
            for i in range(b - t):
                val = matrix[t][t + i]
                matrix[t][t + i] = matrix[b - i][t]
                matrix[b - i][t] = matrix[b][b - i]
                matrix[b][b - i] = matrix[t + i][b]
                matrix[t + i][b] = val
            t += 1
            b -= 1
