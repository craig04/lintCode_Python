class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        if not nums:
            return 0
        max = nums[0]
        sum = 0
        for n in nums:
            sum += n
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max
