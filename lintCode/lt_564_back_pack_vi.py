class Solution:
    """
    @param: nums: an integer array and all positive numbers, no duplicates
    @param: target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        count = [0] * (target + 1)
        count[0] = 1
        for i in xrange(target):
            for n in nums:
                if i + n <= target:
                    count[i + n] += count[i]
        return count[target]
