class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if nums[m] >= target:
                r = m
            else:
                l = m
        return l if nums[l] == target else r if nums[r] == target else -1
