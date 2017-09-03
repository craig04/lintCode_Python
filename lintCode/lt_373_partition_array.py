class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] & 1 != 0:
                l += 1
            while l < r and nums[r] & 1 == 0:
                r -= 1
            if l < r:
                self.__swap(nums, l, r)

    def __swap(self, A, i, j):
        A[i] ^= A[j]
        A[j] ^= A[i]
        A[i] ^= A[j]
