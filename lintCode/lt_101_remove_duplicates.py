class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        rec = None
        length = 0
        for i in range(len(A)):
            if i == 0 or A[i] != A[i - 2]:
                if rec is not None:
                    A[length] = rec
                    length += 1
                rec = A[i]
        if rec:
            A[length] = rec
            length += 1
        return length
