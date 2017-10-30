class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """

    def findMin(self, nums):
        total = sum(nums)
        bound = total >> 1
        made = [True] + [False] * bound
        for n in nums:
            for x in xrange(bound, n - 1, -1):
                made[x] |= made[x - n]
        for n in xrange(bound, -1, -1):
            if made[n]:
                return total - (n << 1)
