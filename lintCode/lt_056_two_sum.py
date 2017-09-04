class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        s = {}
        for i in range(0, len(numbers)):
            s[numbers[i]] = i
        for i in range(0, len(numbers)):
            index = s.get(target - numbers[i])
            if index is not None:
                return [min(i, index) + 1, max(i, index) + 1]
        return None
