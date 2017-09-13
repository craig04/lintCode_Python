class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param: A: An integer list
    @param: queries: An query list
    @return: The result list
    """

    def intervalSum(self, A, queries):
        result = []
        bit = self.__build(A)
        for q in queries:
            result.append(self.__query(bit, q.end + 1) - self.__query(bit, q.start))
        return result

    def __lowBit(self, n):
        return n & -n

    def __build(self, A):
        n = len(A) + 1
        bit = [0] * n
        for i in range(1, n):
            j = i
            while j < n:
                bit[j] += A[i - 1]
                j += self.__lowBit(j)
        return bit

    def __query(self, bit, n):
        result, i = 0, n
        while i:
            result += bit[i]
            i -= self.__lowBit(i)
        return result
