class Solution:
    """
    @param: n: Given the range of numbers
    @param: k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        result = []
        self.__combine(n, k, 0, result, [])
        return result

    def __combine(self, n, k, i, result, s):
        if n == i or k == 0:
            if k == 0:
                result.append(tuple(s))
            return
        s.append(i + 1)
        self.__combine(n, k - 1, i + 1, result, s)
        s.pop()
        if n != k:
            self.__combine(n, k, i + 1, result, s)
