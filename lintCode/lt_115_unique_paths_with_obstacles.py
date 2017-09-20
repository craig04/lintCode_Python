class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        paths = [[0] * (col + 1) for _ in range(row + 1)]
        paths[0][1] = 1
        for i in xrange(row):
            for j in xrange(col):
                paths[i + 1][j + 1] = 0 if obstacleGrid[i][j] == 1 else \
                    paths[i + 1][j] + paths[i][j + 1]
        return paths[row][col]
