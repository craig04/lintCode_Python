class Solution:
    """
    @param A : An integer array
    @return : An integer
    """

    def singleNumberII(self, A):
        a = b = 0
        for c in A:
            a = (a ^ c) & ~b
            b = (b ^ c) & ~a
        return a
