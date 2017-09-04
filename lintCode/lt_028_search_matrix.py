class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):

        row = len(matrix)
        if not row:
            return False
        col = len(matrix[0])
        l = 0
        r = row * col
        while l != r:
            m = (l + r) >> 1
            mid = matrix[m / col][m % col]
            if mid == target:
                return True
            if mid > target:
                r = m
            else:
                l = m + 1
        return False
