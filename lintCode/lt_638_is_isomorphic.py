class Solution:
    """
    @param: s: a string
    @param: t: a string
    @return: true if the characters in s can be replaced to get t or false
    """

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        maps = {}
        used = set()
        for i in xrange(len(s)):
            if t[i] in maps:
                if maps[t[i]] != s[i]:
                    return False
            elif s[i] in used:
                return False
            else:
                used.add(s[i])
                maps[t[i]] = s[i]
        return True
