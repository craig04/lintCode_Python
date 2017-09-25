class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        val = [0] * (m + 1)
        for i in xrange(len(A)):
            for j in range(m, A[i] - 1, -1):
                val[j] = max(val[j], val[j - A[i]] + V[i])
        return max(val)
