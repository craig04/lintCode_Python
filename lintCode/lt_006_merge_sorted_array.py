class Solution:
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        merged = []
        while A and B:
            if A[0] < B[0]:
                merged.append(list.pop(A, 0))
            else:
                merged.append(list.pop(B, 0))
        if B:
            A = B
        while A:
            merged.append(list.pop(A, 0))
        return merged
