class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        min = nums[0]
        sum = 0
        for n in nums:
            sum += n
            if sum < min:
                min = sum
            if sum > 0:
                sum = 0
        return min
