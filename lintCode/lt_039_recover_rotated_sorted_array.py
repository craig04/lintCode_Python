class Solution:
    """
    @param: nums: An integer
    @return:
    """

    def recoverRotatedSortedArray(self, nums):
        length = len(nums)
        i = 0
        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                break
        else:
            return
        self.__reverse(nums, 0, i)
        self.__reverse(nums, i, length)
        self.__reverse(nums, 0, length)

    def __reverse(self, nums, left, right):
        l, r = left, right - 1
        while l < r:
            tempVal = nums[l]
            nums[l] = nums[r]
            nums[r] = tempVal
            l, r = l + 1, r - 1
