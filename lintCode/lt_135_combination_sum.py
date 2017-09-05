class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(set(candidates), reverse=True)
        result = []
        self.__combine(result, candidates, target, [], 0, 0)
        return result

    def __combine(self, result, c, target, l, s, i):
        if i == len(c) or s == target:
            if s == target:
                result.append(sorted(l))
            return
        count = (target - s) / c[i]
        self.__combine(result, c, target, l, s, i + 1)
        for j in range(0, count):
            l.append(c[i])
            s += c[i]
            self.__combine(result, c, target, l, s, i + 1)
        s -= c[i] * count
        del l[len(l) - count:]
