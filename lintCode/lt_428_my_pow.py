class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """

    def myPow(self, x, n):
        f = n < 0
        n = abs(n)
        base = x
        result = 1
        while n:
            if n & 1:
                result *= base
            n >>= 1
            base *= base
        if f:
            result = 1.0 / result
        return result
