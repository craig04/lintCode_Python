class Solution:
    """
    @param: n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        result = []
        self.__generate(n, n, [], result)
        return result

    def __generate(self, l, r, p, result):
        if not l and not r:
            result.append(''.join(p))
            return
        if l:
            p.append('(')
            self.__generate(l - 1, r, p, result)
            p.pop()
        if l != r:
            p.append(')')
            self.__generate(l, r - 1, p, result)
            p.pop()
