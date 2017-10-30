class Solution:
    """
    @param: : a 2d boolean array
    @param: : an integer
    @return: the number of Islands
    """

    def numsofIsland(self, grid, k):
        count = 0
        n = len(grid)
        m = len(grid[0])
        flag = [[False] * m for _ in range(n)]
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in xrange(n):
            for j in xrange(m):
                if self.__dfs(grid, flag, i, j, n, m, move) >= k:
                    count += 1
        return count

    def __dfs(self, grid, flag, r, c, n, m, move):
        if flag[r][c] or grid[r][c] == 0:
            return 0
        count = 1
        flag[r][c] = True
        for x, y in move:
            i, j = r + x, c + y
            if 0 <= i < n and 0 <= j < m:
                count += self.__dfs(grid, flag, i, j, n, m, move)
        return count
