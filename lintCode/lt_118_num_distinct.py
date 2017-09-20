class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        row = len(S)
        col = len(T)
        if row < col:
            return 0
        num = [[1] * (col + 1) for _ in range(row + 1)]
        for i in xrange(col):
            num[i + 1][i + 1] = num[i][i] if S[i] == T[i] else 0
        for r in xrange(row):
            for c in xrange(min(r, col)):
                num[r + 1][c + 1] = num[r][c + 1] + num[r][c] if S[r] == T[c] else 0
        return num[-1][-1]
