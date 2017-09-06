class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if not row:
            return 0
        col = len(matrix[0])
        if not col:
            return 0
        count = 0
        r, c = 0, col - 1
        while r < row and c >= 0:
            val = matrix[r][c]
            if val == target:
                count += 1
            if val <= target:
                r += 1
            if val >= target:
                c -= 1
        return count
