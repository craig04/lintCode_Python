class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        index = -1
        ai, bi = m - 1, n - 1
        while ai != -1 and bi != -1:
            if A[ai] < B[bi]:
                A[index] = B[bi]
                bi -= 1
            else:
                A[index] = A[ai]
                ai -= 1
            index -= 1
        [C, ci] = [A, ai] if ai != -1 else [B, bi]
        while ci != -1:
            A[index] = C[ci]
            ci -= 1
            index -= 1
