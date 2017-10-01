class Solution:
    """
    @param: n: the integer to be reversed
    @return: the reversed integer
    """

    def reverseInteger(self, n):
        neg = n < 0
        res = 0
        n = abs(n)
        maxint = 1 << 32 - 1
        while n:
            res = res * 10 + n % 10
            n /= 10
        if res > maxint or res < -maxint - 1:
            return 0
        return -res if neg else res
