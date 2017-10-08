class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        i1, i2 = 0, len(nums) - 1
        while i1 < i2:
            sums = nums[i1] + nums[i2]
            if sums == target:
                return [i1 + 1, i2 + 1]
            elif sums < target:
                i1 += 1
            else:
                i2 -= 1
        return False
