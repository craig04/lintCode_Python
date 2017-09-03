class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        s = {}
        for n in nums:
            s[n] = s.get(n, 0) + 1
        v = s.items()
        v.sort(key=lambda e: e[0])
        result = []
        self.__makeSubset(v, 0, result, [])
        return result

    def __makeSubset(self, items, i, result, selected):
        if i == len(items):
            list.append(result, list(selected))
            return
        item = items[i]
        self.__makeSubset(items, i + 1, result, selected)
        for j in range(0, item[1]):
            list.append(selected, item[0])
            self.__makeSubset(items, i + 1, result, selected)
        for j in range(0, item[1]):
            list.pop(selected, -1)
