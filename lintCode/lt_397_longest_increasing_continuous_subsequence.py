class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        rev = list(A)
        rev.reverse()
        return max(self.__longest(A), self.__longest(rev))

    def __longest(self, A):
        begin, end = 0, len(A)
        longest = i = 0
        while i < end:
            i = begin + 1
            while i < end:
                if A[i - 1] >= A[i]:
                    break
                i += 1
            longest = max(longest, i - begin)
            begin = i
        return longest
