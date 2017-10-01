class Solution:
    """
    @param: : the given array
    @param: : the window size
    @return: the sum of the count of unique elements in each window
    """

    def slidingWindowUniqueElementsSum(self, nums, k):
        k = min(k, len(nums))
        count = {}
        unique = 0
        result = 0
        for i in xrange(len(nums)):
            n = count.setdefault(nums[i], 0)
            unique += 1 if n == 0 else -1 if n == 1 else 0
            count[nums[i]] += 1
            if i >= k - 1:
                result += unique
                r = nums[i - k + 1]
                count[r] -= 1
                t = count[r]
                unique += 1 if t == 1 else -1 if t == 0 else 0
        return result
