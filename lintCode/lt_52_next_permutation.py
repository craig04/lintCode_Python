class Solution:
    # @param nums: a list of integer
    # @return: return nothing (void), do not return anything, modify nums in-place instead
    def nextPermutation(self, nums):
        if not nums:
            return nums
        last = len(nums) - 1
        i = last
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i <= 0:
            list.reverse(nums)
            return
        j = last
        while nums[j] <= nums[i - 1]:
            j -= 1
        self.__swap(nums, i - 1, j)
        j = last
        while i < j:
            self.__swap(nums, i, j)
            i += 1
            j -= 1

    def __swap(self, A, i, j):
        A[i] ^= A[j]
        A[j] ^= A[i]
        A[i] ^= A[j]
