class Solution:
    """
    @param: : the given number
    @return: whether whether there're two integers
    """

    def checkSumOfSquareNumbers(self, num):
        if num < 0:
            return False
        from math import sqrt
        root = int(sqrt(num))
        for i in xrange(root + 1):
            d = num - i * i
            r = int(sqrt(d))
            if d == r * r:
                return True
        return False
