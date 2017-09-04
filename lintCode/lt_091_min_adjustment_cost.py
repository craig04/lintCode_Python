import sys


class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """

    def MinAdjustmentCost(self, A, target):
        num = len(A)
        upper = max(A) + 1
        prev = [abs(i - A[0]) for i in range(upper)]
        for i in range(1, num):
            cur = [sys.maxint] * upper
            for j in range(1, upper):
                b = max(1, j - target)
                e = min(upper, j + target + 1)
                for t in range(b, e):
                    cur[j] = min(cur[j], prev[t] + abs(A[i] - j))
            prev = cur
        return min(prev)
