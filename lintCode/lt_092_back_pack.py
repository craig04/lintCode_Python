class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        dp = [x == 0 for x in range(0, m + 1)]
        for a in A:
            for x in range(m - a, -1, -1):
                dp[x + a] |= dp[x]
        for x in range(m, -1, -1):
            if dp[x]:
                return x
