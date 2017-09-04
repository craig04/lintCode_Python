import sys


class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        nums = [1]
        idx = [0] * 3
        fac = [2, 3, 5]
        for i in range(1, n):
            nxt = sys.maxint
            for j in range(3):
                nxt = min(nxt, nums[idx[j]] * fac[j])
            nums.append(nxt)
            for j in range(3):
                if nums[idx[j]] * fac[j] == nxt:
                    idx[j] += 1
        return nums[n - 1]
