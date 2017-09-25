class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        length = len(nums)
        if length < 3:
            return min(nums)
        mid = length >> 1
        b = nums[0]
        m = nums[mid]
        e = nums[-1]
        if b > m:
            return self.findMin(nums[:mid + 1])
        if m > e:
            return self.findMin(nums[mid:])
        if b == m and m == e:
            return min(nums)
        return nums[0]
