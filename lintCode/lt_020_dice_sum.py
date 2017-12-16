class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        init = [1 / 6.0] * 6
        for i in range(1, n):
            length = len(init)
            t = [0] * (length + 5)
            for j in range(6):
                for k in range(length):
                    t[k + j] += init[k] / 6
            init = t
        return [(i, init[i - n]) for i in range(n, 6 * n + 1)]
