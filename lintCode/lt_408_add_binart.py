class Solution:
    """
    @param: a: a number
    @param: b: a number
    @return: the result
    """

    def addBinary(self, a, b):
        f, c, i = 0, str(), 0
        lenA, lenB = len(a), len(b)
        for i in xrange(-1, -max(lenA, lenB) - 1, -1):
            ta = self.__get(a, i, lenA)
            tb = self.__get(b, i, lenB)
            f += ta + tb
            c += str(f & 1)
            f >>= 1
        c += ('1' if f else '')
        return c[::-1]

    def __get(self, s, i, lenS):
        return 0 if i < -lenS else int(s[i])
