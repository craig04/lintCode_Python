class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, candidates, target):
        result = set()
        self.__combine(candidates, target, [], 0, 0, result)
        return list(result)

    def __combine(self, candidates, target, l, s, i, result):
        if i == len(candidates) or s >= target:
            if s == target:
                lst = list(l)
                lst.sort()
                result.add(tuple(lst))
            return
        self.__combine(candidates, target, l, s, i + 1, result)
        l.append(candidates[i])
        self.__combine(candidates, target, l, s + candidates[i], i + 1, result)
        l.pop()
