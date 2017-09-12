class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        nums = [1]
        for i in range(1, n + 1):
            count = 0
            for j in range(0, i):
                count += nums[j] * nums[i - j - 1]
            nums.append(count)
        return nums[-1]
