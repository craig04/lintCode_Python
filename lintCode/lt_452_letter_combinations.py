class Solution:
    """
    @param: digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        con = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        self.__generate(digits, 0, result, [], con)
        return result

    def __generate(self, digits, i, result, s, con):
        if i == len(digits):
            if s:
                result.append(''.join(s))
            return
        for d in con[int(digits[i])]:
            s.append(d)
            self.__generate(digits, i + 1, result, s, con)
            s.pop()
