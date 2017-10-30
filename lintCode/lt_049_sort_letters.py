class Solution:
    """
    @param chars: The letters array you should sort.
    """

    def sortLetters(self, chars):
        n = len(chars)
        b, e = 0, n - 1
        sorts = [''] * n
        for c in chars:
            if str.islower(c):
                sorts[b] = c
                b += 1
            else:
                sorts[e] = c
                e -= 1
        for i in xrange(n):
            chars[i] = sorts[i]
