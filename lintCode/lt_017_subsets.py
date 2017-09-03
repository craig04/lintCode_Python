class Solution:
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        result = []
        nums.sort()
        self.__subsets(nums, 0, result, [])
        return result

    def __subsets(self, nums, i, result, selected):
        if i == len(nums):
            result.append(list(selected))
            return
        self.__subsets(nums, i + 1, result, selected)
        selected.append(nums[i])
        self.__subsets(nums, i + 1, result, selected)
        selected.pop()
