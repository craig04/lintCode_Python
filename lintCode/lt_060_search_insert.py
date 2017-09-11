class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        l, r = 0, len(A)
        while l < r:
            m = (l + r) >> 1
            mid = A[m]
            if mid < target:
                l = m + 1
            elif mid > target:
                r = m
            else:
                return m
        return l
