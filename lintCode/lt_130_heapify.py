class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        n = len(A)
        for i in xrange(n / 2 - 1, -1, -1):
            n = len(A)
            t = i
            while t < n / 2:
                m = t * 2 + 1
                if m + 1 < n and A[m + 1] < A[m]:
                    m += 1
                if A[m] >= A[t]:
                    break
                temp = A[t]
                A[t] = A[m]
                A[m] = temp
                t = m
