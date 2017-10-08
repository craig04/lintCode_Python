class Solution:
    """
    @param: : an integer
    @return:  the factorial of n
    """

    def factorial(self, n):
        return str(reduce(lambda x, y: x * y, range(1, n + 1), 1))
