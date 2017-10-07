class Solution:
    """
    @param: : the prices
    @param: : the length of rod
    @return: the max value
    """

    def cutting(self, prices, n):
        val = [0] * (n + 1)
        length = 1
        for p in prices:
            for i in xrange(length, n + 1):
                val[i] = max(val[i], val[i - length] + p)
            length += 1
        return max(val)
