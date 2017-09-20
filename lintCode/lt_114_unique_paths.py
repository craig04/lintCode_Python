class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        k = min(m, n)
        n += m - 1
        c = [[1] * k for _ in range(n)]
        for i in xrange(1, n):
            for j in xrange(1, min(i, k)):
                last = c[i - 1]
                c[i][j] = last[j] + last[j - 1]
        return c[n - 1][k - 1]
