import bisect


class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        li = {}
        for i in range(len(B) - 1, -1, -1):
            li.setdefault(B[i], []).append(i)
        indices = []
        for c in A:
            indices.extend(li.get(c, []))
        values = []
        for n in indices:
            i = bisect.bisect_left(values, n)
            if i == len(values):
                values.append(0)
            values[i] = n
        return len(values)
