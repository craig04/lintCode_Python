class Solution:
    """
    @param: n: An integer
    @return: True or false
    """

    def checkPowerOf2(self, n):
        return n > 0 and n == n & -n
