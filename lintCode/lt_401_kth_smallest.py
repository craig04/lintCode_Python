import heapq


class Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """

    def kthSmallest(self, matrix, k):
        row = len(matrix)
        col = len(matrix[0])
        heap = [[matrix[0][0], 0, 0]]
        flag = [[False] * col for i in range(row)]
        while k != 0:
            k -= 1
            val, i, j = heapq.heappop(heap)
            if not k:
                return val
            if i != row - 1 and not flag[i + 1][j]:
                flag[i + 1][j] = True
                heapq.heappush(heap, [matrix[i + 1][j], i + 1, j])
            if j != col - 1 and not flag[i][j + 1]:
                flag[i][j + 1] = True
                heapq.heappush(heap, [matrix[i][j + 1], i, j + 1])
        return None
