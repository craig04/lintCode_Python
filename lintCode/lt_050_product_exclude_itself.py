class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, nums):

        length = len(nums)
        if length == 1:
            return [1]
        product = 1
        front = [1]
        for n in nums:
            product *= n
            front.append(product)
        product = 1
        back = [1]
        for i in range(-1, -length, -1):
            product *= nums[i]
            back.append(product)
        result = []
        for i in range(0, length):
            result.append(front[i] * back[length - i - 1])
        return result
