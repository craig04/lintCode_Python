class Solution:
    """
    @param: : a number
    @param: : digit needed to be rorated
    @return: a number
    """

    def leftRotate(self, n, d):
        mask = (1 << 32) - 1
        rotate = n << d
        return ((rotate & ~mask) >> 32) | (rotate & mask)
