class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """

    def longestCommonSubstring(self, A, B):
        lenA, lenB = len(A) + 1, len(B) + 1
        dp = [[0] * lenB for i in range(lenA)]
        for i in range(1, lenA):
            for j in range(1, lenB):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(dp, key=lambda e: max(e)))
