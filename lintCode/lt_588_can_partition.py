class Solution:
    """
    @param: nums: a non-empty array only positive integers
    @return: true if can partition or false
    """

    def canPartition(self, nums):
        sums = sum(nums)
        if sums & 1 != 0:
            return False
        half = sums >> 1
        maxn = max(nums)
        if maxn > half:
            return False
        elif maxn == half:
            return True
        flag = [n == 0 for n in xrange(half + 1)]
        for n in nums:
            if flag[half - n]:
                return True
            for i in xrange(half, n - 1, -1):
                flag[i] |= flag[i - n]
            print flag
        return flag[half]
