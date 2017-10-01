class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        return self.__break(s, dict, {"": 1})

    def __break(self, s, dict, cache):
        if s in cache:
            return cache[s]
        count = 0
        for i in xrange(1, len(s) + 1):
            if s[:i] in dict:
                count += self.__break(s[i:], dict, cache)
        cache[s] = count
        return count
