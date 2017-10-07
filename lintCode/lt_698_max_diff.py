class Solution:
    """
    @param: : an array of arrays
    @return: return the max distance among arrays
    """

    def maxDiff(self, arrs):
        result = 0
        mins = arrs[0][0]
        maxs = arrs[0][-1]
        for i in xrange(1, len(arrs)):
            result = max(result, maxs - arrs[i][0])
            result = max(result, arrs[i][-1] - mins)
            mins = min(mins, arrs[i][0])
            maxs = max(maxs, arrs[i][-1])
        return result
