class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        n = len(grid)
        m = len(grid[0])
        if not n or not m:
            return 0
        sums = [[set()] * (m + 1) for _ in range(n + 1)]
        sums[0][1] = {0}
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                s = set(sums[i - 1][j])
                s.update(sums[i][j - 1])
                sums[i][j] = set(val + grid[i - 1][j - 1] for val in s)
        return reduce(lambda x, y: x + y, sums[-1][-1], 0)
