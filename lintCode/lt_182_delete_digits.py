class Solution:
    """
    @param: A: A positive integer which has N digits, A is a string
    @param: l: Remove k digits
    @return: A string
    """

    def DeleteDigits(self, A, l):
        return str(int(self.__delete(A, len(A) - l)))

    def __delete(self, A, k):
        if k == 0:
            return ''
        index = -1
        digit = 10
        for i in xrange(len(A) - k + 1):
            val = int(A[i])
            if val < digit:
                index = i
                digit = val
        return A[index] + self.__delete(A[index + 1:], k - 1)
