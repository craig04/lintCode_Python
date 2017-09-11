import bisect


class Solution:
    """
    @param: A: An integer array
    @param: queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """

    def countOfSmallerNumber(self, A, queries):
        list.sort(A)
        result = []
        for q in queries:
            result.append(bisect.bisect_left(A, q))
        return result
