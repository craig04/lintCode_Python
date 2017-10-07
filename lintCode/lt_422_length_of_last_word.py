class Solution:
    """
    @param: s: A string
    @return: the length of last word
    """

    def lengthOfLastWord(self, s):
        last = len(s) - 1
        for i in range(-1, -1 - len(s), -1):
            if s[i] == ' ' and last < 0:
                return last - i
            elif s[i] != ' ' and last >= 0:
                last = i
        return len(s) - last - 1
