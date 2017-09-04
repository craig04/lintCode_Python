class Solution:
    # @param A: An integers list.
    # @return: return any of peek positions.

    def findPeak(self, A):
        for i in range(2, len(A)):
            if A[i] < A[i - 1]:
                return i - 1
        return None
