class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        length = 0
        for i in range(len(A)):
            if i == 0 or A[i] != A[i - 1]:
                A[length] = A[i]
                length += 1
        return length
