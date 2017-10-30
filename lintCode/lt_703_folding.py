class Solution:
    """
    @param: : the original array
    @param: : the direction each time
    @return: the final folded array
    """

    def folding(self, nums, req):
        nums = [nums]
        for r in req:
            fold = []
            n = len(nums)
            m = len(nums[0]) >> 1
            a, b, c, d = [0, m, m, m * 2] if r == 0 else [m, m * 2, 0, m]
            for i in xrange(n - 1, -1, -1):
                fold.append(list(reversed(nums[i][a:b])))
            for i in xrange(n):
                fold.append(nums[i][c:d])
            nums = fold
        return map(lambda e: e[0], nums)
