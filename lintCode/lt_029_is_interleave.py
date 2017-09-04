class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """

    def isInterleave(self, s1, s2, s3):
        len1 = len(s1)
        len2 = len(s2)
        if len1 + len2 != len(s3):
            return False
        dp = [[True] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(len1):
            dp[i + 1][0] = dp[i][0] and s1[i] == s3[i]
        for j in range(len2):
            dp[0][j + 1] = dp[0][j] and s2[j] == s3[j]
        for i in range(len1):
            for j in range(len2):
                dp[i + 1][j + 1] = (dp[i][j + 1] and s1[i] == s3[i + j + 1]) or (
                    dp[i + 1][j] and s2[j] == s3[i + j + 1])
        return dp[len1][len2]
