import bisect


class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        values = []
        for n in nums:
            i = bisect.bisect_left(values, n)
            if i == len(values):
                values.append(0)
            values[i] = n
        return len(values)
