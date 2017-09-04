class Solution:
    """
    @param: A: An integer array
    @return: An integer array
    """

    def singleNumberIII(self, A):
        a = b = xor = 0
        for n in A:
            xor ^= n
        bit = xor & -xor
        for n in A:
            if bit & n:
                a ^= n
            else:
                b ^= n
        return [a, b]
