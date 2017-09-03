class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if not nums:
            return [[]]
        result = list()
        list.sort(nums)
        while True:
            result.append(list(nums))
            j = len(nums) - 1
            while j > 0:
                if nums[j] > nums[j - 1]:
                    break
                j -= 1
            if j == 0:
                break
            k = len(nums) - 1
            while nums[k] <= nums[j - 1]:
                k -= 1
            self.__swap(nums, j - 1, k)
            k = len(nums) - 1
            while j < k:
                self.__swap(nums, j, k)
                j += 1
                k -= 1
        return result

    def __swap(self, l, i, j):
        l[i] ^= l[j]
        l[j] ^= l[i]
        l[i] ^= l[j]
