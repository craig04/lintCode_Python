class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        zeros = 0
        while n != 0:
            n /= 5
            zeros += n
        return zeros
