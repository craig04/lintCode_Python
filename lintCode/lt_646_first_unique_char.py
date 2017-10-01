class Solution:
    """
    @param: s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        count = {}
        for c in s:
            count[c] = count.setdefault(c, 0) + 1
        for i in xrange(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
