class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        mid = len(nums) >> 1
        return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))
