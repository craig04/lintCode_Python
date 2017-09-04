class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        xor = 0
        for n in A:
            xor ^= n
        return xor
