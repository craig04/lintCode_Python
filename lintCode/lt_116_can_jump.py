class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        farthest = 0
        length = len(A)
        reach = [not i for i in range(length)]
        for i in range(length):
            if not reach[i]:
                return False
            f = min(length, A[i] + i + 1)
            if f == length:
                return True
            while farthest < f:
                reach[farthest] = True
                farthest += 1
