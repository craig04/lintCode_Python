class Solution:
    """
    @param: A: An integer array
    """

    def __init__(self, A):
        n = len(A)
        self.__A = [0] * n
        self.__bit = [0] * (n + 1)
        for i in range(n):
            self.modify(i, A[i])

    def __lowBit(self, n):
        return n & -n

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """

    def query(self, start, end):
        return self.__query(end + 1) - self.__query(start)

    def __query(self, n):
        result, i = 0, n
        while i:
            result += self.__bit[i]
            i -= self.__lowBit(i)
        return result

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """

    def modify(self, index, value):
        delta = value - self.__A[index]
        self.__A[index] = value
        j = index + 1
        while j < len(self.__bit):
            self.__bit[j] += delta
            j += self.__lowBit(j)
