class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        result = []
        nums = numbers
        nums.sort()
        length = len(nums)
        i = 0
        while i < length:
            l = i + 1
            r = length - 1
            while l < r:
                left = nums[l]
                right = nums[r]
                if left + right == -nums[i]:
                    single = [left, right, nums[i]]
                    single.sort()
                    result.append(single)
                if left + right <= -nums[i]:
                    l = self.__jump(nums, l, length, 1)
                if left + right >= -nums[i]:
                    r = self.__jump(nums, r, -1, -1)
            i = self.__jump(nums, i, length, 1)
        return result

    @staticmethod
    def __jump(numbers, i, end, step):
        j = i
        while j != end:
            if numbers[j] != numbers[i]:
                return j
            j += step
        return end
