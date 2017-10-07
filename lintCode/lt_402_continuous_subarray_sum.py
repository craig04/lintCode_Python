class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        sums = 0
        maxs = A[0]
        begin = 0
        result = [0, 0]
        for i in range(len(A)):
            sums += A[i]
            if maxs < sums:
                maxs = sums
                result = [begin, i]
            elif sums < 0:
                sums = 0
                begin = i + 1
        return result
