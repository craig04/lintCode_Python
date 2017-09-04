class Solution:
    """
    @param: s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        p = []
        match = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                p.append(c)
            elif not p or p.pop() != match[c]:
                return False
        return not p
