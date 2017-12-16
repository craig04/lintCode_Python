from math import sqrt, ceil


class Solution:
    """
    @param n: the given number
    @return: true if it has exactly three distinct factors, otherwise false
    """

    def isThreeDisctFactors(self, n):
        r = int(ceil(sqrt(n)))
        return r * r == n and self._isPrime(r)

    def _isPrime(self, n):
        r = int(ceil(sqrt(n)))
        for i in xrange(2, r):
            if n % i == 0:
                return False
        return n > 1
