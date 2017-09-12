class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if not n:
            return 0
        a, b = 0, 1
        for i in range(n + 1):
            c = a + b
            a = b
            b = c
        return a
