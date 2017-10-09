class Solution:
    """
    @param: s: a string
    @param: t: a string
    @return: true if they are both one edit distance apart or false
    """

    def isOneEditDistance(self, s, t):
        lens = len(s)
        lent = len(t)
        if abs(lens - lent) >= 2:
            return False
        if lens == lent:
            return len(filter(None, map(lambda x, y: x == y, s, t))) == lens - 1
        for i in xrange(min(lens, lent)):
            if s[i] != t[i]:
                break
        else:
            i = min(lens, lent)
        return s[i + 1:] == t[i:] if lens > lent else s[i:] == t[i + 1:]
