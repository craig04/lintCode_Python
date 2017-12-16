class Solution:
    """
    @param: : a number
    @return: return the next sparse number behind x
    """

    def nextSparseNum(self, x):
        if self.__isSparse(x):
            return x
        import math
        high = 1 << int(math.floor(math.log(x, 2)))
        halfHigh = high >> 1
        doubleHigh = high << 1
        if x & halfHigh:
            return doubleHigh
        rec = self.nextSparseNum(x & ~high)
        if rec == halfHigh:
            return doubleHigh
        return high | rec

    def __isSparse(self, x):
        if x == 0:
            return True
        low = 0
        while x:
            bit = x & -x
            if bit == low << 1:
                return False
            x &= ~bit
            low = bit
        return True
