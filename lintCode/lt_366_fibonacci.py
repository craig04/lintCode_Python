class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        return 0 if n == 1 else 1 if n == 2 else self.__fibonacci(n)

    def __fibonacci(self, n):
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
