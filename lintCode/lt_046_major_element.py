class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums):
        count = 1
        major = nums[0]
        for i in range(1, len(nums)):
            if major == nums[i]:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    major = nums[i]
        return major
