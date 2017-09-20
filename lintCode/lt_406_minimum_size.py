from sys import maxint


class Solution:
    """
    @param: nums: an array of integers
    @param: s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        sums = 0
        begin = 0
        result = maxint
        for i in xrange(0, len(nums)):
            sums += nums[i]
            if sums <= 0:
                sums = 0
                begin = i + 1
                continue
            elif sums >= s:
                while sums - nums[begin] >= s:
                    sums -= nums[begin]
                    begin += 1
                result = min(result, i - begin + 1)
        return result if result != maxint else -1
