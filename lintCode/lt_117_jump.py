class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        length = len(A)
        farthest = 1
        jumps = [0] * length
        for i in range(length - 1):
            f = min(length, A[i] + i + 1)
            if f == length:
                return A[i] + 1
            while farthest < f:
                jumps[farthest] = jumps[i] + 1
                farthest += 1
        return jumps[-1]
